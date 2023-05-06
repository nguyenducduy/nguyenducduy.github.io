---
layout: page
permalink: /about/index.html
title: I'm Duy
tags: [Duy, Duy Nguyen, Nguyễn Đức Duy]
imagefeature: fourseasons.jpg
chart: true
---
<figure>
  <img src="{{ site.url }}/images/nguyen-duc-duy.jpg" alt="Nguyễn Đức Duy" width="30%">
  <figcaption>Nguyễn Đức Duy -  Coder</figcaption>
</figure>

{% assign total_words = 0 %}
{% assign total_readtime = 0 %}
{% assign featuredcount = 0 %}
{% assign statuscount = 0 %}

{% for post in site.posts %}
    {% assign post_words = post.content | strip_html | number_of_words %}
    {% assign readtime = post_words | append: '.0' | divided_by:200 %}
    {% assign total_words = total_words | plus: post_words %}
    {% assign total_readtime = total_readtime | plus: readtime %}
    {% if post.featured %}
    {% assign featuredcount = featuredcount | plus: 1 %}
    {% endif %}
{% endfor %}


Tui là Duy, tui làm blog này để chia sẻ những kinh nghiệm cũng như những kiến thức hay ho về công nghệ lập trình web. Tui hồi mới bắt đầu đi làm tới giờ cũng đã hơn 10 năm (2014-2023) tính tới thời điểm tui bắt đầu viết blog này. Nếu bạn đang theo dõi tui thì chắc chắn bạn đang muốn trở thành một Fullstack Developer, nghĩa là một người lập trình viên có thể code nhiều mảng khác nhau của một ứng dụng, và chúc mừng bạn, bạn đã tìm được người có thể sẵn sàng hỗ trợ bạn, một người đồng hành cùng bạn trên con đường lập trình đầy thú vị này nha.

Khởi điểm của tui cũng như bao người khác, thậm chí không bằng những bạn bây giờ, cũng đi học chuyên ngành công nghệ thông tin tại [NIIT](https://www.niit.com/vietnam/), tốt nghiệp hệ Cao Đẳng thời bấy giờ thì cũng tạm được, học được 1 chút kiến thức những công nghệ Microsoft như VB, ASP, Excel, Access, MSSQL, ... nhưng cơ bản là không có hứng thú lắm và quyết định học thêm ngôn ngữ lập trình [PHP](https://www.php.net/) thì thấy là khá "dính" với nó. Quyết định tầm sư học đạo với thầy [Võ Duy Tuấn](https://vn.linkedin.com/in/voduytuan) và cùng thầy đi chinh chiến tại [Điện máy Xanh](https://www.dienmayxanh.com/), khởi đầu cho chuỗi ngày ăn dằm nằm dề với code.

<figure class="half">
	<a href="{{ site.url }}/images/about/dienmayxanh/4_members.jpg"><img src="{{ site.url }}/images/about/dienmayxanh/4_members.jpg"></a>
	<a href="{{ site.url }}/images/about/dienmayxanh/all_members.jpg"><img src="{{ site.url }}/images/about/dienmayxanh/all_members.jpg"></a>
	<figcaption>Chinh chiến tại dienmay.com năm 2014 (Bây giờ là dienmayxanh.com)</figcaption>
</figure>


Tui làm việc tại [Điện máy Xanh](https://www.dienmayxanh.com/) với role PHP-DevOps, lúc này thì chẳng biết role này là gì, không hiểu tại sao học code PHP mà vô ngồi bắt làm việc với server Linux, rất may là được anh Thế Anh (SysAdmin của [TGDĐ](https://www.thegioididong.com/)) hướng dẫn và chỉ dạy nhiệt tình nên cũng dần thẩm thấu được 1 chút kiến thức về quản trị server Linux. Công việc hằng ngày lúc đó chủ yếu là đọc sách và theo dõi, tối ưu hệ thống xoay quanh những thứ như caching và load balancing.

Và cái gì tới rồi cũng sẽ tới, thầy tui có lối đi riêng nên đành giã từ [Điện máy Xanh](https://www.dienmayxanh.com/), khởi nghiệp với [Teamcrop](https://www.teamcrop.com/) - Nền tảng quản lý chuỗi bán lẻ trên web. Lúc này thì càng áp lực hơn vì phải tự setup server vật lý, rồi vác nó đặt lên VDC Datacenter, thiết lập VPN, CI/CD Jenkins, ... không có ai cứu cánh, phải tự lực cánh sinh nhưng cũng rất là thú vị. Khởi nghiệp lun là 1 thứ gì đó vô cùng hấp dẫn và chông gai.

<figure class="half">
	<a href="{{ site.url }}/images/about/teamcrop/working_together.png"><img src="{{ site.url }}/images/about/teamcrop/working_together.png"></a>
	<a href="{{ site.url }}/images/about/teamcrop/all_members.jpg"><img src="{{ site.url }}/images/about/teamcrop/all_members.jpg"></a>
</figure>
<figure class="third">
	<a href="{{ site.url }}/images/about/teamcrop/IMG_0128.JPG"><img src="{{ site.url }}/images/about/teamcrop/IMG_0128.JPG"></a>
	<a href="{{ site.url }}/images/about/teamcrop/IMG_0129.JPG"><img src="{{ site.url }}/images/about/teamcrop/IMG_0129.JPG"></a>
	<a href="{{ site.url }}/images/about/teamcrop/IMG_0130.JPG"><img src="{{ site.url }}/images/about/teamcrop/IMG_0130.JPG"></a>
	<figcaption>Khởi nghiệp cùng thầy tại Spiral (teamcrop.com) năm 2015. Vất vả nhưng được cái nó vui.</figcaption>
</figure>


Lúc này setup server xong thì ngồi chơi cưỡi ngựa xem hoa, rảnh rỗi nhớ code nên cũng tập tành ngồi viết 1 cái starter-kit dựa trên 1 framework PHP mới ra lúc bấy giờ là [Phalcon (C-extension)](https://phalcon.io/en-us) với ưu điểm là siêu nhanh và ngốn ít resource nhất. Bây giờ thì đã cũ rồi, nếu các bạn muốn vẫn có thể clone về để tham khảo nha [Phalcon Jumpstart](https://github.com/nguyenducduy/phalcon-jumpstart) & [PHP framework starter](https://github.com/nguyenducduy/php-framework-starter).


Năm 2016, quản trị server hoài cũng nhàn nên tui quyết định bay lượn ở vùng trời khác, tui gia nhập [5giay.vn](https://www.5giay.vn/) lúc đó là sàn rao vặt thời kỳ đầu dưới dạng forum với lượng truy cập rất cao (bây giờ thì sụp rồi), muốn nâng cấp từ vBulltetin lên Xenforo và build 1 trang rao vặt đúng nghĩa. Project đã hoàn thành nhưng vì nhiều lý do không thể duy trì và phát triển được (không có nhân lực, thuê sinh viên làm lại nên bây giờ thành cái web xấu xí nhất quả đất). Tui đành chia tay 5giay, tui đi phỏng vấn và đậu 1 số cty như Mainspring (hiện sở hữu bởi ByteDance - Cty mẹ của ứng dụng TikTok), Tiki.vn, KynaForKid, Siêu Việt Group (Chủ sở hữu 1 số website tìm việc), HDWebsoft, ... nhưng phong cách làm việc và dự án ở đây có lẽ không phù hợp với tui và cuối cùng tui tìm thấy [OLLI](https://olli.vn/): với ý tưởng điên rồ và táo bạo thời điểm đó, tui gia nhập và tự nâng cấp bản thân mình cho đến bây giờ.

<figure class="third">
	<a href="{{ site.url }}/images/about/olli/IMG_0008.JPG"><img src="{{ site.url }}/images/about/olli/IMG_0008.JPG"></a>
	<a href="{{ site.url }}/images/about/olli/IMG_0109.jpg"><img src="{{ site.url }}/images/about/olli/IMG_0109.jpg"></a>
	<a href="{{ site.url }}/images/about/olli/IMG_0020.JPG"><img src="{{ site.url }}/images/about/olli/IMG_0020.JPG"></a>
	<figcaption>OLLI - Những thành viên thuở sơ khai, làm việc tại Lutaco Tower</figcaption>
</figure>
<figure class="third">
	<a href="{{ site.url }}/images/about/olli/IMG_4651.JPG"><img src="{{ site.url }}/images/about/olli/IMG_4651.JPG"></a>
	<a href="{{ site.url }}/images/about/olli/IMG_4949.JPG"><img src="{{ site.url }}/images/about/olli/IMG_4949.JPG"></a>
	<a href="{{ site.url }}/images/about/olli/IMG_4819.JPG"><img src="{{ site.url }}/images/about/olli/IMG_4819.JPG"></a>
	<figcaption>OLLI - CES ASIA Shanghai trip (Đi dự triển lãm công nghệ CES tại Thượng Hải, TQ. Tiện đi du lịch lun)</figcaption>
</figure>
<figure>
	<a href="{{ site.url }}/images/about/olli/IMG_0120.JPG"><img src="{{ site.url }}/images/about/olli/IMG_0120.JPG"></a>
	<figcaption>Vâng. Tui ngồi đây và tui có thể làm những gì tui thích. (Thực ra là tui ngồi đối diện sếp tui =.=", còn ảnh ngồi ngay chỗ tui đứng chụp) </figcaption>
</figure>

Đến với [OLLI](https://olli.vn/), như một duyên số nào đó đã gắn chặt tui ở đây, vì ở đây tui cảm thấy thoải mái, cảm thấy được quan tâm và được làm 1 dự án rất là hay ho. Được dẫn dắt bởi 2 người trẻ nhưng có hoài bão lớn, sứ mệnh mang lại 1 sản phẩm tốt và hữu ích dành cho người Việt, đó là [Loa thông minh Maika](https://olli.vn/products/loa-thong-minh-maika). Công việc của tui chủ yếu ở đây là quản lý về kỹ thuật những vấn đề liên quan đến mảng nội dung của loa Maika, nói thì ngắn gọn vậy thôi chứ xoay quanh nó rất nhiều kỹ thuật và vấn đề phát sinh mà tui sẽ chia sẻ trong blog này.

Các bạn theo dõi nhé.

Thân, Duy coder.