---
layout: post
title: "Làm map 3D bằng AI: AI giỏi ở hai đầu, khúc giữa vẫn cần người"
description: "Tui mày mò làm map 3D với AI một thời gian. AI sinh cả thế giới thì đẹp mà chưa xài được, còn chỗ nó giúp thật thì lại nằm ở những khúc ít ai để ý."
headline: 
date: 2026-11-15 20:00:00 +0700
modified: 2026-11-15
category: AI
tags: [ai, 3d, gamedev, map]
imagefeature: map3d/cover.jpg
mathjax: 
chart: 
comments: true
featured: true
---

Dạo này mạng xã hội toàn video kiểu "gõ một câu, AI sinh ra cả thế giới 3D đi vô được". Coi xong ai cũng nghĩ làm map game giờ chắc chỉ cần ngồi gõ prompt. Tui cũng nghĩ vậy, nên lao vô thử.

Thử một thời gian thì tui rút ra một chuyện: **AI giúp được nhiều lắm, nhưng không phải ở chỗ mọi người hay tưởng.** Bài này tui ghi lại cách tui đang làm, chỗ nào AI đỡ việc thật, chỗ nào vẫn phải tự tay.

## Một cái map 3D gồm những gì

{% include figure.html src="map3d/layers.jpg" alt="Các lớp của một map 3D: địa hình, khối lắp ghép, cây cỏ rải theo luật, điểm nhấn" caption="Map thật thường là nhiều lớp chồng lên nhau, mỗi lớp làm bằng một cách." class="small" %}

Trước khi nói chuyện AI, phải hiểu map được dựng ra sao. Đại khái có mấy cách:

- **Bản đồ độ cao (heightmap):** một tấm ảnh xám, chỗ sáng là núi, chỗ tối là thung lũng. Rẻ, sửa nhanh, hợp đồi núi đồng ruộng. Nhưng không làm được hang hay vách lõm.
- **Điêu khắc nguyên khối:** nặn cả map như nặn đất sét trong Blender. Tự do, nhưng khó sửa và nặng khi map lớn.
- **Bộ lắp ghép:** tường, mái, cầu, bậc thang ghép lại như Lego. Hợp làm thành, chùa, hầm ngục.
- **Rải theo luật:** cây mọc ở chỗ thoải, đá nằm ở sườn dốc, cỏ phủ chỗ còn lại. Sửa luật là sửa cả map.

Game lớn như Horizon, Ghost of Tsushima hay Genshin đều trộn mấy cách này: địa hình làm nền, rải theo luật cho phần rộng, còn mấy điểm nhấn quan trọng thì người đặt tay.

## AI "sinh cả thế giới" giờ tới đâu rồi

{% include figure.html src="map3d/aiworld.jpg" alt="Một thế giới 3D do AI sinh ra, đẹp nhưng mờ ảo và không có đường đi" caption="Đẹp thì đẹp thiệt, nhưng đi vô đâu được." class="small" %}

Tui có coi và thử mấy cái tên đang nổi:

- [Marble](https://www.worldlabs.ai/blog/marble-world-model) của World Labs: từ chữ hoặc ảnh ra cả một cảnh 3D. Xuất ra mesh thì khoảng 600 ngàn tới 1 triệu tam giác ([thông số](https://docs.worldlabs.ai/marble/export/specs.md)). Mỗi thế giới tốn khoảng 1,2–1,3 USD, xuất mesh chất lượng cao thêm 2,8 USD ([bảng giá](https://docs.worldlabs.ai/api/pricing)).
- [HY-World 2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) của Tencent: mở trọng số, nhưng cần card NVIDIA đời mới, model rất nặng, và [giấy phép](https://github.com/Tencent-Hunyuan/HY-World-2.0/blob/main/License.txt) không áp dụng cho EU, Anh, Hàn Quốc.
- [Matrix-3D](https://github.com/SkyworkAI/Matrix-3D): từ ảnh ra ảnh toàn cảnh, ra video, rồi ra đám điểm 3D. Không có mesh.
- [Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/) của Google: đi vô được thiệt, nhưng thứ nó tạo ra là video tương tác, tối đa khoảng một phút.

Nhìn demo thì mê, nhưng đem vô game thì vướng ba chuyện. Một là **quá nặng**: một cảnh AI sinh ra nặng gấp mấy lần mức máy điện thoại tầm trung chạy nổi. Hai là **không có "luật chơi"**: không có đường đi rõ ràng, không biết chỗ nào đứng được, chỗ nào là vách. Ba là **giấy phép và giá** còn nhiều ràng buộc.

Nên tới thời điểm này, tui chỉ dùng mấy cái này làm **ảnh tham khảo hình khối**, giống như nhờ AI phác thảo ý tưởng.

## Chỗ AI giúp thật: hai đầu quy trình

Cái hay là AI giúp rất nhiều ở **đầu vào** và ở **từng món đồ**.

Ở đầu vào, AI đỡ nhiều nhất ở hai việc: ra địa hình và rải đồ vật.

**Ra địa hình.** Nhờ AI vẽ một tấm **concept sa bàn** (một ảnh nhìn chéo cả map, như nhìn mô hình trên bàn), cho một model đo độ sâu (tui dùng MoGe) đoán chỗ nào cao chỗ nào thấp, rồi chuyển thành bản đồ độ cao thô. Cách này hợp khi concept là một khối đất gọn gàng. Còn map lớn cần đúng tỉ lệ thì tui phác vùng bằng số liệu (khu nào ở đâu, cao bao nhiêu) rồi cho script dựng địa hình. Lúc đó tấm concept chỉ để duyệt cảm giác.

{% include figure.html src="map3d/concept.jpg" alt="Tấm concept sa bàn do AI vẽ: núi đá, thác nước, ruộng bậc thang, làng và sân đấu trên một hòn đảo giữa mây" caption="Tấm concept AI vẽ để duyệt cảm giác. Đẹp vậy chứ không đúng tỉ lệ, nên tui không dùng nó để đo đạc." class="small" %}

**Rải đồ vật.** Phần này tui làm vầy:

1. Dựng địa hình xong, chụp một tấm từ trên xuống. Lúc này map còn trơ trọi.
2. Cho AI vẽ lại tấm ảnh đó **hai lần**: lần đầu thêm nội dung (rừng, đá, nhà, cầu), lần sau mới đổi phong cách. Gộp hai yêu cầu vô một lần thì model hay làm một việc rồi quên việc kia.
3. Cho AI nhận diện từng vật trong ảnh: GroundingDINO tìm khung theo chữ ("cây tùng, nhà, cầu..."), SAM2 cắt viền cho chính xác. Hai món này chạy ngay trên máy, khoảng một phút, không tốn đồng nào.
4. Tui ngồi duyệt lại một tờ ảnh đánh số, sửa mấy chỗ AI nhận sai. Ví dụ có cái cột đá bị nó nhận là cây tùng.
5. Tính ngược từ điểm ảnh ra toạ độ thật trên địa hình, rồi đặt model vào đúng chỗ.

Lượt đầu ra gần 1.000 món đồ trên một map 640 × 640 mét, tui chỉ còn kéo thả chỉnh lại. Sau đó tui thay cây và người bằng model làm riêng, chạy lại một lượt thì lên gần 1.900 món. Khúc cuối là phần rải theo luật: hàng trà chạy theo sườn đồi, rào làng, ao, ruộng bậc thang, thác nước ở mép đảo, đều sinh bằng script nên sửa luật là cả map đổi theo. Chừng đó món mà tự tay đặt từng cái thì mỏi tay lắm.

<figure>
	<video controls muted playsinline preload="metadata" poster="{{ site.url }}/images/map3d/tour-poster.webp" width="1280" height="720">
		<source src="{{ site.url }}/images/map3d/tour.mp4" type="video/mp4">
		Trình duyệt của bạn không phát được video này. <a href="{{ site.url }}/images/map3d/tour.mp4">Tải video về xem</a>.
	</video>
	<figcaption>Bay một vòng map sau khi làm xong, quay trong game (40 giây): toàn cảnh, làng, chợ, bậc đá lên núi, sân đấu, rừng, đồi trà, ruộng, ao và thác nước.</figcaption>
</figure>

Có một chuyện vui: hồi thử nguyên chuỗi Matrix-3D, tui thấy khúc đáng giá nhất lại chỉ là bước đo độ sâu ở giữa, mà bước đó chạy ngon trên Mac luôn. Mấy bước sinh video với đám điểm nặng nề phía sau thì bỏ được.

Còn với từng món đồ như cái nhà, cây cầu, tảng đá, thì AI làm rất ổn. Hunyuan3D, Tripo biến ảnh thành model 3D, rồi nhờ AI vẽ lại texture cho đúng phong cách. [Tripo giờ còn tách được từng vật](https://www.cgchannel.com/2026/10/tripo-integrates-gpt-image-2-5-sunburst-into-its-image-to-3d-workflow/) ra khỏi một tấm ảnh concept cả cảnh, đỡ công vẽ lẻ từng món.

Mảng bản đồ độ cao cũng đang có nghiên cứu hay như [MESA](https://mikonvergence-mesa.hf.space/) hay [Terrain Diffusion](https://arxiv.org/abs/2512.08309), gõ chữ ra địa hình. Tui đang để mắt, chưa xài thật.

## Khúc giữa vẫn phải tự tay

{% include figure.html src="map3d/blockout.jpg" alt="Đi thử nhân vật trên bản map khối thô để kiểm tra đường đi và độ dốc" caption="Map khối thô xấu hoắc, nhưng phải đi thử trên đó trước khi trang trí." class="small" %}

Phần giữa là phần làm nên cái "vui" của map, và AI chưa hiểu được chuyện này.

- **Dựng khối thô rồi đi thử bằng nhân vật thật**, đúng tốc độ, đúng độ cao nhảy, chứ đừng bay camera ngắm. Lỗi hay gặp nhất là sai tỉ lệ, và bản khối thô đầu tiên hầu như không sống nổi qua lần chơi thử đầu ([Level Design Book](https://book.leveldesignbook.com/process/blockout)).
- **Đặt một điểm nhấn kéo người chơi đi tới**: một ngọn tháp, một cái cây to, nhìn thấy từ xa. Dân làm game gọi vui là ["wienie"](https://www.above-the-garage.com/wienies/), học từ cách Disneyland đặt lâu đài. Zelda: Breath of the Wild còn có cả luật tam giác: núi lớn làm mốc, núi vừa che tầm nhìn, gò nhỏ tạo nhịp ([bản dịch bài nói CEDEC 2017](https://gist.github.com/idbrii/e39fe96279aa1670319bfa521d907399)).
- **Rải theo luật nhưng người cầm lái**: Horizon Zero Dawn để máy rải cây cỏ, còn họa sĩ chỉ viết luật và chỉnh ([Guerrilla](https://www.guerrilla-games.com/read/gpu-based-procedural-placement-in-horizon-zero-dawn)). Muốn dời con đường thì vẽ lại đường, cây tự dạt ra.

AI đưa tui bản nháp, nhưng đường đi chỗ nào dốc quá, chỗ nào trống quá, chỗ nào người chơi sẽ lạc, thì phải tự đi mới biết.

## Đừng quên mấy cái máy yếu

Đây là cái bẫy lớn nhất mà tui thấy ít ai nói: **map đẹp mà máy chạy không nổi thì cũng bằng không.**

Theo hướng dẫn của [Epic](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-and-development-best-practices-for-mobile-projects-in-unreal-engine) và [Unity cùng Arm](https://unity.com/blog/games/tackling-profiling-for-mobile-games-with-unity-and-arm), máy tầm trung chạy 30 khung hình mỗi giây chỉ chịu nổi khoảng 500–700 lệnh vẽ và cỡ 500 ngàn đỉnh mỗi khung. Một cảnh AI sinh ra đã vượt mức đó vài lần.

Mấy game thế giới mở trên điện thoại xử lý bằng vài mẹo quen thuộc: chia map thành ô, chỉ tải ô gần người chơi; vật ở xa thay bằng bản rút gọn hoặc tấm ảnh giả 3D; bóng đổ ở xa tính sẵn hoặc cập nhật thưa. Mà nói gì thì nói, **đo trên máy thật** mới là thước cuối.

## Nhưng cũng đừng tưởng bở

AI làm map đang tiến nhanh thiệt, vài tháng lại có model mới. Nhưng demo đẹp khác với đem vô sản phẩm. Trước khi xài cái gì, tui luôn hỏi ba câu: **nặng cỡ nào, giấy phép cho làm gì, và có đi vô chơi được không**. Trả lời được cả ba thì mới đáng bỏ công.

Còn cái tư duy "gõ một câu ra cả game" thì tui nghĩ còn xa. Thứ đang có thật là AI làm phụ tá rất giỏi: phác thảo nhanh, làm đồ nhanh, còn mình giữ phần quyết định cái gì vui, cái gì chạy nổi.

## Vậy bắt đầu từ đâu?

Nếu bạn muốn thử làm map 3D với AI, tui gợi ý vầy: nhờ AI vẽ một tấm concept sa bàn, cho model đo độ sâu biến nó thành địa hình thô, dựng khối thô rồi tự đi thử trên đó. Xong phần đó rồi mới nhờ AI làm từng món đồ để trang trí. Làm theo thứ tự này thì đỡ phí công hơn nhiều so với lao vô sinh cả thế giới ngay từ đầu.

Mấy bài sau tui sẽ kể kỹ hơn từng bước, kèm mấy lỗi té sấp mặt trong lúc làm. Các bạn theo dõi nha.

Thân, Duy viber.
