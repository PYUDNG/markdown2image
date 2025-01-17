# 看图<br>
自定义图库的随机图片分发器

## 用法<br>
### 看图相关功能<br>
- `#run 看图`<br>
  从默认图库中随机输出一张图片<br>
  没有设置过默认图库时，从被最多用户设为默认的图库中随机输出一张图片<br>
- `#run 看图 图库名`<br>
  从指定图库输出随机图片<br>
- `#run 看图 图片类型 图片值`<br>
  不添加到任何图库，直接看图

### 图库编辑功能<br>
用来列出、查看、创建、修改图库<br>

- `#run 看图 +图库名 图片类型 图片值`<br>
  将新的图片添加到指定图库<br>
  有关**图片类型**和**图片值**:<br>
  - 目前支持三种图片类型：`pixiv`、`link`和`md`<br>
  - `pixiv`<br>
    p站的图片，添加时以pixiv图片的id作为图片值<br>
    比如，<u>https://www.pixiv.net/artworks/91087340</u>的图片值为`91087340`<br>
  - `link`<br>
    网络图片的链接，要求是直接能访问的直链，通常时图床提供的链接，或者图片API的链接<br>
  - `md`<br>
    展示自定义markdown<br>
  - **组图**的图片值<br>
    可以将多张图片作为一组同时录入到一个图片值中，输出时会一起输出同一图片值中的所有图片。这样的多张图片录入时，需要将所有图片的图片值以英文逗号`","`拼接，组合成这一组图的图片值。组图录入示例:<br>
    `#run 看图 +图库名 pixiv 1111111,2222222,333333` 将三张pixiv图片`1111111`、`2222222`、`3333333`作为一组图录入

  如需一次添加多张图片，可以以每行一个图片值的格式录入:<br>
  <code><br>
  #run 看图 -- +图库名 图片类型<br>
  图片1值<br>
  图片2值<br>
  图片3值<br>
  图片4值<br>
  </code><br>
  注意：一次性添加多张图片时，所有图片的类型必须一致<br>

- `#run 看图 -图库名 图片类型 图片值`<br>
  从指定图库中删除指定图片<br>
  如需一次删除多张图片，格式和上面添加多张图片类似<br>
- `#run 看图 -图库名 %图片序号`<br>
  根据图片序号从指定图库中删除指定图片，图片序号指的是使用「`list 图库名`」命令时，图片列表中方括号中的数字<br>
  按照图片序号删除图片目前尚未支持批量删除多张图片<br>
- `#run 看图 +新图库名`<br>
  新建一个空图库<br>
- `#run 看图 -图库名`<br>
  删除一个已有图库<br>
- `#run 看图 #源图库名 新图库名`<br>
  复制一个已有的图库为新图库<br>
- `#run 看图 %旧图库名 新图库名`<br>
  更改一个已有图库的名字<br>
- `#run 看图 list`<br>
  列出所有图库<br>
- `#run 看图 list 图库名`<br>
  列出指定图库的所有图片<br>
- `#run 看图 list 图库名 页码`<br>
  列出指定图库的所有图片，按照页码输出（每页10条）<br>
- `#run 看图 info 图库名`<br>
  查看指定图库的属性<br>
- `#run 看图 info 图库名 属性名 属性值`<br>
  更改指定图库的属性<br>
  支持设置的属性值:<br>
  - `描述`/`desc`/`description`<br>
    字面意思，图库的描述信息

### 默认图库功能<br>
每个用户都可以设置自己的默认图库，设置后，运行`#run 看图`时将从自己的默认图库中输出<br>
如果没有设置过默认图库，将会把被最多人设置为默认图库的图库作为默认图库使用<br>

- `#run 看图 default 图库名`<br>
  将指定图库设置为默认图库<br>
- `#run 看图 default`<br>
  查看当前默认图库<br>
- `#run 看图 !default`<br>
  清除默认图库设置

### 其他命令<br>
- `#run 看图 history`<br>
  查看最近看图历史<br>
- `#run 看图 (help|--help|-h|帮助)`<br>
  输出此帮助文档并退出

<script>
    const colors = ['red', 'green', 'blue', 'red', 'green', 'blue'];
    const footer = document.createElement('div');
    footer.style.width = '100vw';
    footer.style.backgroundColor = 'transparent';
    footer.style.position = 'absolute';
    footer.style.left = '0';
    document.body.append(footer);
    for (const color of colors) {
        const line = document.createElement('div');
        line.style.width = '100vw';
        line.style.height = '1px';
        line.style.backgroundColor = color;
        footer.append(line);
    }
</script>