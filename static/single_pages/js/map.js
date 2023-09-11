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

naver.maps.Event.addListener(map, "click", function (e) {
  // 클릭라인 연결하기
  var point = e.coord;
  var path = polyline.getPath();
  path.push(point);

  var marker = new naver.maps.Marker({
    position: e.coord,
    map: map,
  });

  markerList.push(marker);
  marker.setPosition(point);
});

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
});

// 클릭라인 연결하기
var polyline = new naver.maps.Polyline({
  map: map,
  path: [],
  strokeColor: "#82d8d9",
  strokeWeight: 5,
});

// 정보창
var contentString = ["#정보 넣을곳"].join("");
var infowindow = new naver.maps.InfoWindow({
  content: contentString,
  maxWidth: 140,
  backgroundColor: "#f5f5f5",
  borderColor: "#82d8d9",
  borderWidth: 5,
  anchorSize: new naver.maps.Size(30, 30),
  anchorSkew: true,
  anchorColor: "#55555",
  pixelOffset: new naver.maps.Point(20, -20),
});
naver.maps.Event.addListener(marker, "click", function (e) {
  if (infowindow.getMap()) {
    infowindow.close();
  } else {
    infowindow.open(map, marker);
  }
});

// 마커표시 이동
