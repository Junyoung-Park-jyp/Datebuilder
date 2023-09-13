document.addEventListener("DOMContentLoaded", function() {
  var selectedData = []; // 선택한 카드의 데이터를 저장할 배열

  // 선택하기 버튼을 클릭할 때
  document.querySelector(".pickcourse").addEventListener("click", function() {
      // 선택한 카드의 데이터 수집 및 JSON 형식으로 가공
      var data = {
          subject: "카드 제목", // 선택한 카드의 제목 데이터
          content: "카드 내용"  // 선택한 카드의 내용 데이터
      };

      // 수집한 데이터를 배열에 추가
      selectedData.push(data);

      // 선택한 카드의 데이터를 JSON 문자열로 변환하여 숨겨진 필드에 설정
      document.querySelector("#selected_data").value = JSON.stringify(selectedData);
  });
});