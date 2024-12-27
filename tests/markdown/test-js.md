<script>
    // 在这里传入游戏配置和棋盘数据
    const data = {
        width: 9,
        defaultColor: '#3B3B3B',
        playerColor: ['#CC6600', '#6666FF'],
        playerData: [
            [1, 5, 13],
            [81, 77, 69]
        ],
        curPlayer: 1
    };
</script>

<style>
    body {
        background-color: #292929;
    }
    .hex, .hex::after, .hex::before {
        border-top: 1px solid #8E8E8E;
        border-bottom: 1px solid #8E8E8E;
    }
    .hex {
        width: 50px;
        height: 86.6px;
        position: relative;
        margin: -1px 13px;
        display: block;
        user-select: none;
        cursor: pointer;
    }
    .hex.p1, .hex.p2 {
        cursor: default;
    }
    .hex::after, .hex::before {
        position: absolute;
        left: 0;
        top: 0;
        content: '';
        width: 50px;
        height: 86.6px;
        background-color: inherit;
    }
    .hex::after{
        transform: rotate(60deg);
    }
    .hex::before{
        transform: rotate(-60deg);
    }
    .number {
        display: flex;
        color: #f0f0f0;
        z-index: 1;
        position: relative;
        height: 100%;
        width: 100%;
        align-items: center;
        justify-content: center;
        font-size: 40px;
    }
    .board {
        display: flex;
        margin-left: 20px;
        margin-right: 20px;
    }
    .col {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
<div class="board" id="board"></div>

<script>
    (function() {
        // 落子历史
        const history = [];
        // 悔棋历史
        const regretHistory = [];

        // 创建n*n的棋盘，由于存在边框，实际需要画(n+2)*(n+2)的格子
        data.width += 2;

        // 创建棋盘
        let number = 0;
        let hexes = {};
        const board = document.querySelector('#board');
        for (let i = 0; i < data.width * 2 - 1; i++) {
            // 当前列有几个hex方格
            const n = i < data.width ? i + 1 : data.width * 2 - i - 1;

            // 创建col列
            const col = document.createElement('div');
            col.classList.add('col');
            board.append(col);
            
            // 创建hex六边形方格
            for (let j = 0; j < n; j++) {
                // 方格外层六边形外壳
                const hex = document.createElement('div');
                hex.classList.add('hex');

                // 每一列第一格和最后一格是边框，不属于游戏区域，没有编号、不参与交互
                const isBorder = j === 0 || j == n - 1;
                if (isBorder) {
                    // 边框
                    if (i === 0 || i == data.width * 2 - 2) {
                        playerClass = 'p1';
                    } else if (i == data.width - 1) {
                        playerClass = 'p2';
                    } else {
                        playerClass = j === 0 ?
                            (i < data.width ? 'p1' : 'p2') :
                            (i < data.width ? 'p2' : 'p1');
                    }
                    hex.classList.add(playerClass);
                } else {
                    // 非边框
                    // 数字编号
                    number++;

                    // 显示编号
                    const num_outer = document.createElement('div');
                    num_outer.classList.add('number');
                    const num_inner = document.createElement('div');
                    num_inner.innerText = number.toString();
                    num_outer.append(num_inner);
                    hex.append(num_outer);

                    // 记录编号对应格子
                    hexes[number] = hex;
                }

                // 添加到棋盘中
                col.append(hex);
            }
        }

        // 游戏数据
        for (let i = 0; i < data.playerData.length; i++) {
            const player = data.playerData[i];
            const playerClass = `p${i+1}`;
            player.forEach(num => hexes[num].classList.add(playerClass));
        }
        board.setAttribute('player', data.curPlayer.toString());

        // 颜色css
        let css = [
            `.hex { background-color: ${data.defaultColor}; }`,
            `.hex.p1, [player="1"] .hex:not(.p1, .p2):hover { background-color: ${data.playerColor[0]}; }`,
            `.hex.p2, [player="2"] .hex:not(.p1, .p2):hover { background-color: ${data.playerColor[1]}; }`,
            `.hex:hover:not(.p1, .p2) { filter: grayscale(0.6) brightness(1.15); }`
        ];
        const style = document.createElement('style');
        style.innerHTML = css.join('\n');
        document.head.append(style);

        // 点击下棋
        let curPlayer = 1;
        board.addEventListener('click', e => {
            if (!e.target.matches) { return; }
            if (e.target.matches(':is(:not(.hex, .hex *), .p1, .p2, :is(.p1, .p2) *)')) { return; }

            let hex = e.target;
            while (!hex.matches('.hex')) {
                hex = hex.parentElement;
            }

            place(hex, curPlayer);
        }, { capture: true });

        // Ctrl-Z 悔棋; Ctrl-Shift-Z 反向悔棋
        document.body.addEventListener('keydown', e => {
            if (e.ctrlKey && String.fromCharCode(e.keyCode).toUpperCase() === 'Z') {
                if (e.shiftKey) {
                    reverseRegret();
                } else {
                    regret();
                }
            }
        });

        function place(hex, player) {
            hex.classList.add(`p${ player.toString() }`);
            switchPlayer();
            const step = { hex, player };
            history.push(step);
            regretHistory.splice(0, regretHistory.length);
            return step;
        }

        function regret() {
            if (!history.length) { return; }
            const step = history.pop();
            step.hex.classList.remove(`p${ step.player.toString() }`);
            switchPlayer();
            regretHistory.push(step);
            return step;
        }

        function reverseRegret() {
            if (!regretHistory.length) { return; }
            const step = regretHistory.pop();
            step.hex.classList.add(`p${ step.player.toString() }`);
            switchPlayer();
            history.push(step);
            return step;
        }

        function switchPlayer() {
            curPlayer = curPlayer == 1 ? 2 : 1;
            board.setAttribute('player', curPlayer.toString());
        }
    }) ();
</script>
