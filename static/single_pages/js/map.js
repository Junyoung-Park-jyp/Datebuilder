// 마커표시
var position = new naver.maps.LatLng(37.5112, 127.0981);
var HOME_PATH = window.HOME_PATH || ".";

var map = new naver.maps.Map("map", {
  center: position,
  zoom: 15,
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
