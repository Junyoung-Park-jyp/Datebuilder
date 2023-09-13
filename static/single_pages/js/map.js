// 마커표시
var position = new naver.maps.LatLng(37.5665, 126.978);
// 행정구역 설정
var HOME_PATH = window.HOME_PATH || ".";

var map = new naver.maps.Map("map", {
  center: position,
  zoom: 10,
});

var marker = new naver.maps.Marker({
  position: position,
  map: map,
});

var markerList = [];
var menuLayer = $(
  '<div style="position:absolute;z-index:10000;background-color:#fff;border:solid 1px #333;padding:10px;display:none;"></div>'
);

map.getPanes().floatPane.appendChild(menuLayer[0]);

// 클릭이벤트
naver.maps.Event.addListener(map, "click", function (e) {
  markerList.push(marker);
  marker.setPosition(e.coord);
  var feature = e.feature;
  var regionName = feature.getProperty("area_name"); // 행정구역 이름으로 변경

  if (feature.getProperty("focus") !== true) {
    feature.setProperty("focus", true);

    // 클릭한 행정구역에 대한 정보 표시
    alert("선택한 행정구역: " + regionName);
  } else {
    feature.setProperty("focus", false);
  }
});
// 키다운 이벤트
naver.maps.Event.addListener(map, "keydown", function (e) {
  var keyboardEvent = e.keyboardEvent,
    keyCode = keyboardEvent.keyCode || keyboardEvent.which;

  var ESC = 27;

  if (keyCode === ESC) {
    keyboardEvent.preventDefault();

    for (var i = 0, ii = markerList.length; i < ii; i++) {
      markerList[i].setMap(null);
    }

    markerList = [];
    menuLayer.hide();
  }
});
// 마우스다운이벤트
naver.maps.Event.addListener(map, "mousedown", function (e) {
  menuLayer.hide();
});

naver.maps.Event.addListener(map, "rightclick", function (e) {
  var coordHtml =
    "Coord: " + "(우 클릭 지점 위/경도 좌표)" + "<br />" + "Point: " + e.point + "<br />" + "Offset: " + e.offset;

  menuLayer
    .show()
    .css({
      left: e.offset.x,
      top: e.offset.y,
    })
    .html(coordHtml);

  console.log("Coord: " + e.coord.toString());

  // 마커표시 이동

  // 클릭라인 연결하기
  var point = e.coord;
  var path = polyline.getPath();
  path.push(point);

  var marker = new naver.maps.Marker({
    position: e.coord,
    map: map,
  });
});

// 클릭라인 연결하기
var polyline = new naver.maps.Polyline({
  map: map,
  path: [],
  strokeColor: "#82d8d9",
  strokeWeight: 5,
});

// 정보창
var contentString = [
  '<div class="iw_inner">',
  "   <h3>{ 가게명 }</h3>",
  "   <p>{주소}<br />",
  '       <img src="' + HOME_PATH + '/img/example/.jpg" width="55" height="55" alt="" class="thumb" /><br />',
  "       {전화번호} | { 종류 }<br />",
  '       <a href="#" target="_blank">{사이트}</a>',
  "   </p>",
  "</div>",
].join("");
var infowindow = new naver.maps.InfoWindow({
  content: contentString,
  maxWidth: 400,
  backgroundColor: "#f5f5f5",
  borderColor: "#82d8d9",
  borderWidth: 5,
  anchorSize: new naver.maps.Size(30, 50),
  anchorSkew: false,
  anchorColor: "#82d8d9",
  pixelOffset: new naver.maps.Point(20, -20),
});
naver.maps.Event.addListener(marker, "click", function (e) {
  if (infowindow.getMap()) {
    infowindow.close();
  } else {
    infowindow.open(map, marker);
  }
});

// 행정구역 설정

// 서울 행정구역 경계 데이터를 regionGeoJson 배열에 추가
$.ajax({
  url: "",
  success: function (geojson) {
    regionGeoJson.push(geojson);
    loadCount++;

    if (loadCount === 1) {
      startDataLayer();
    }
  },
});

// startDataLayer 함수에서 스타일링 및 이벤트 처리를 진행합니다.
function startDataLayer() {
  // 행정구역 스타일링 설정
  map.data.setStyle(function (feature) {
    var styleOptions = {
      fillColor: "#ff0000",
      fillOpacity: 0.3,
      strokeColor: "#ff0000",
      strokeWeight: 2,
      strokeOpacity: 0.8,
    };

    if (feature.getProperty("focus")) {
      styleOptions.fillOpacity = 0.6;
      styleOptions.fillColor = "#0f0";
      styleOptions.strokeColor = "#0f0";
      styleOptions.strokeWeight = 4;
      styleOptions.strokeOpacity = 1;
    }

    return styleOptions;
  });

  // 행정구역 데이터 추가
  regionGeoJson.forEach(function (geojson) {
    map.data.addGeoJson(geojson);
  });
  // 툴팁 및 마우스 이벤트 리스너 등은 그대로 사용 가능
}
