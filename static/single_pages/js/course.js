document.addEventListener("DOMContentLoaded", function() {
    // 카드를 클릭할 때 발생하는 이벤트 리스너
    document.querySelectorAll(".card").forEach(function(card) {
        card.addEventListener("click", function() {
            // 클릭한 카드의 데이터 ID 가져오기
            var dataId = card.getAttribute("data-data-id");

            // 서버로 데이터 ID를 전송하기 위한 AJAX 요청
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "/single_pages/createcourse/?data_id=" + dataId, true);

            xhr.onload = function() {
                if (xhr.status === 200) {
                    // 서버에서 받은 응답을 처리
                    var response = JSON.parse(xhr.responseText);
                    // 여기에서 서버에서 반환한 데이터를 사용하거나 처리할 수 있습니다.
                    console.log(response);
                }
            };

            xhr.send();
        });
    });
});
