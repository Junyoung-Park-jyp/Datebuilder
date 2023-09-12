// document.addEventListener("DOMContentLoaded", function() {
//     // 카드를 클릭할 때 발생하는 이벤트 리스너
//     document.querySelectorAll(".modal").forEach(function(card) {
//         card.addEventListener("click", function() {
//             // 클릭한 카드의 데이터 ID 가져오기
//             var dataId = card.getAttribute("data-data-id");

//             // 서버로 데이터 ID를 전송하기 위한 AJAX 요청
//             var xhr = new XMLHttpRequest();
//             xhr.open("GET", "/single_pages/createcourse/?data_id=" + dataId, true);

//             xhr.onload = function() {
//                 if (xhr.status === 200) {
//                     // 서버에서 받은 응답을 처리
//                     var response = JSON.parse(xhr.responseText);
//                     // 여기에서 서버에서 반환한 데이터를 사용하거나 처리할 수 있습니다.
//                     console.log(response);
//                 }
//             };

//             xhr.send();
//         });
//     });
// });
document.addEventListener("DOMContentLoaded", function() {
    var selectedDataIds = []; // 선택한 데이터 ID를 저장할 배열

    // 카드를 클릭할 때 발생하는 이벤트 리스너
    document.querySelectorAll(".modal").forEach(function(modal) {
        modal.addEventListener("click", function() {
            // 클릭한 카드의 데이터 ID 가져오기
            var dataId = modal.getAttribute("data-data-id");
            
            // 선택한 데이터 ID를 배열에 추가
            selectedDataIds.push(dataId);

            // 선택한 데이터 ID가 3개인 경우 서버로 전송
            if (selectedDataIds.length === 3) {
                // 서버로 데이터 ID 배열을 전송하기 위한 AJAX 요청
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/single_pages/createcourse/", true);
                xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

                xhr.onload = function() {
                    if (xhr.status === 200) {
                        // 서버에서 받은 응답을 처리
                        var response = JSON.parse(xhr.responseText);
                        // 여기에서 서버에서 반환한 데이터를 사용하거나 처리할 수 있습니다.
                        console.log(response);
                    }
                };

                // 배열을 서버로 전송
                xhr.send(JSON.stringify(selectedDataIds));

                // 선택한 데이터 ID 배열 초기화
                selectedDataIds = [];
            }
        });
    });
});
