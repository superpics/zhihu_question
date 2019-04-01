#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff
from plotly.graph_objs import Figure, Layout, Bar
from scrapy import Selector
from w3lib.html import remove_tags

if __name__ == "__main__":
    htmlStr = """<p><b>我，男，普通人。</b></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p>自身情况：</p><p>坐标清远（广清公积金互贷能不能算广州啊喂！），男，90年，体长170，体重60，单位带编，到手4k综合10k，有被动收入数额不多（最近还停了悲惨）明年大概上升到150k吧没什么想法哈哈是比较少，最近做了些很烧钱的事情就不说了。在财政大院长大童年超幸福，现在越来越惨变得不爱说话，市区有房有铺有车有车位，长得还行，以前经常打dota现在王者狼人杀，偶尔锻炼下厨，三年单身，单身后没去过旅游一个怕寂寞一个也想和另一半一起去探索世界（原以为能脱单）。考编之后工作日在单位和单位宿舍，周末在家宅，圈子实在是太小，自杀式单身已经没想法和寄托。</p><p class="ztext-empty-paragraph"><br/></p><p><b>不排斥知乎找对象</b></p><p class="ztext-empty-paragraph"><br/></p><p>择偶条件：</p><p>1、经济条件：<b>彼此差不多行了</b>（我是独生，父亲副局长，母亲通信业国企中层领导已退休）（basic+预期，不满足也没什么关系，最好差不多但不能赤贫什么的养不起）</p><p>2、相貌条件：<b>彼此差不多行了</b>（不能纹身）（最好圆脸，喜欢有点肉的（胸大））</p><p>3、生活状态：<b>彼此差不多行了</b>（不抽烟、不酗酒、不劈腿、午晚睡前要刷牙）</p><p>4、未来规划：稳中求进的生活</p><p>5、个人特质：彼此差不多行了（知世故而不世故、杀伐果断、因人而异的善良、有那么一丢丢毅力）（咦这品质是谁？噢，仿佛是我自己）</p><p>6、星座：不天秤座、不水瓶座（主要是遇见这两个星座的同事朋友同学多了实在太克，好难受鸭）</p><p>7、<b>身高学历取消限制</b>，毕竟脑子好使三观正就卡掉很多未婚女青年了，不敢要求（其实本科扩招，限制也没什么作用，满街本科生。大专生也有牛逼的男女青年，只是有些人晚熟，在高考前觉醒不了，觉醒慢了点，考了大专不过是际遇问题，不一定是智力或者努力程度问题，人生很长，都互相理解）（听说什么最佳身高差是12cm，我170希望女方182吧？哈哈哈哈哈哈哈不好笑，溜了）</p><p class="ztext-empty-paragraph"><br/></p><p>感情可以是任何样子，但不喜欢的也会很明确。</p><p>坐标很重要，希望是同一市区</p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p>最后..要不发点旧照吧..</p><figure data-size="normal"><noscript><img src="https://pic1.zhimg.com/50/v2-fdb5417d74004a8f1c61053eaabe0d6f_hd.jpg" data-caption="" data-size="normal" data-rawwidth="640" data-rawheight="960" data-default-watermark-src="https://pic1.zhimg.com/50/v2-fdb5417d74004a8f1c61053eaabe0d6f_hd.jpg" class="origin_image zh-lightbox-thumb" width="640" data-original="https://pic1.zhimg.com/v2-fdb5417d74004a8f1c61053eaabe0d6f_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;640&#39; height=&#39;960&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="640" data-rawheight="960" data-default-watermark-src="https://pic1.zhimg.com/50/v2-fdb5417d74004a8f1c61053eaabe0d6f_hd.jpg" class="origin_image zh-lightbox-thumb lazy" width="640" data-original="https://pic1.zhimg.com/v2-fdb5417d74004a8f1c61053eaabe0d6f_r.jpg" data-actualsrc="https://pic1.zhimg.com/50/v2-fdb5417d74004a8f1c61053eaabe0d6f_hd.jpg"/></figure><figure data-size="normal"><noscript><img src="https://pic2.zhimg.com/50/v2-73a351f8bd92f38f8f3b6d0307217756_hd.jpg" data-caption="" data-size="normal" data-rawwidth="480" data-rawheight="480" data-default-watermark-src="https://pic2.zhimg.com/50/v2-73a351f8bd92f38f8f3b6d0307217756_hd.jpg" class="origin_image zh-lightbox-thumb" width="480" data-original="https://pic2.zhimg.com/v2-73a351f8bd92f38f8f3b6d0307217756_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;480&#39; height=&#39;480&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="480" data-rawheight="480" data-default-watermark-src="https://pic2.zhimg.com/50/v2-73a351f8bd92f38f8f3b6d0307217756_hd.jpg" class="origin_image zh-lightbox-thumb lazy" width="480" data-original="https://pic2.zhimg.com/v2-73a351f8bd92f38f8f3b6d0307217756_r.jpg" data-actualsrc="https://pic2.zhimg.com/50/v2-73a351f8bd92f38f8f3b6d0307217756_hd.jpg"/></figure><figure data-size="normal"><noscript><img src="https://pic4.zhimg.com/50/v2-17e9e18322e17cc582790c5e194a6ae9_hd.jpg" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="1440" data-default-watermark-src="https://pic4.zhimg.com/50/v2-17e9e18322e17cc582790c5e194a6ae9_hd.jpg" class="origin_image zh-lightbox-thumb" width="1080" data-original="https://pic4.zhimg.com/v2-17e9e18322e17cc582790c5e194a6ae9_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1080&#39; height=&#39;1440&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="1440" data-default-watermark-src="https://pic4.zhimg.com/50/v2-17e9e18322e17cc582790c5e194a6ae9_hd.jpg" class="origin_image zh-lightbox-thumb lazy" width="1080" data-original="https://pic4.zhimg.com/v2-17e9e18322e17cc582790c5e194a6ae9_r.jpg" data-actualsrc="https://pic4.zhimg.com/50/v2-17e9e18322e17cc582790c5e194a6ae9_hd.jpg"/></figure><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p><br/>emmm接受私信，在下告辞。</p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p class="ztext-empty-paragraph"><br/></p><p>以上。</p><p></p><p></p>"""


    data = Selector(text=htmlStr)

    imgs = data.xpath("//img/@src").extract()

    # removeTags = remove_tags(a)
    for i in imgs:
        if i.startswith("data"):
            imgs.remove(i)

    for i in imgs:
        print("===> %s" % i)





