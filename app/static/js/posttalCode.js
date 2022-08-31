// //郵便番号検索
// const searchPostalCode = (e) => {
//     console.log('--------------serchPortalStart--------------')
//     // var request = new XMLHttpRequest();
  
//     // var url = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060'
//     // request.open('GET', url, true);
//     // request.responseType = 'json';
  
//     // request.onload = function () {
//     //   var data = this.response;
//     //   console.log(data);
//     // };
  
//     // request.send();
  
//     // var script = document.createElement('script');
//     //   script.src = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060';
//     //   window.instaCallbackFavorites = function(response) {
//     //       // reponseをhogehogeする
//     //   };
//     //   document.body.appendChild(script);
  
//     //入力値をセット
//     // var param = {zipcode: $('#zipcode').val()}
//     //zipcloudのAPIのURL
//     var param = $('#id_postal_code').val()
//     var send_url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + param;
//     $.ajax({
//       type: "GET",
//       cache: false,
//       // data: '7830060',
//       url: send_url,
//       async: false,
//       dataType: "jsonp",
//       success: function (res) {
//         //結果によって処理を振り分ける
//         if (res.status == 200 && res.results !== null) {
//           var result = res.results[0]
//           //処理が成功したとき
//           $('#not-find-toast').toast('hide')
//           $('#prefectures').val(result.address1);
//           $('#municipalities').val(result.address2);
//           $('#address').val(result.address3);
//         } else {
//           //エラーだった時
//           $('#not-find-toast').toast('show')
//           $('#prefectures').val("");
//           $('#municipalities').val("");
//           $('#address').val("");
//         }
//       },
//       error: function (XMLHttpRequest, textStatus, errorThrown) {
//         console.log(XMLHttpRequest);
//       }
//     });
//   }
  
  
  
  
//郵便番号検索
const searchPostalCode = (e) => {
    console.log('--------------serchPortalStart--------------')
    // var request = new XMLHttpRequest();
  
    // var url = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060'
    // request.open('GET', url, true);
    // request.responseType = 'json';
  
    // request.onload = function () {
    //   var data = this.response;
    //   console.log(data);
    // };
  
    // request.send();
  
    // var script = document.createElement('script');
    //   script.src = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060';
    //   window.instaCallbackFavorites = function(response) {
    //       // reponseをhogehogeする
    //   };
    //   document.body.appendChild(script);
  
    //入力値をセット
    // var param = {zipcode: $('#zipcode').val()}
    //zipcloudのAPIのURL
    var param = $('#id_zip1').val() + $('#id_zip2').val();
    var send_url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + param;
    $.ajax({
      type: "GET",
      cache: false,
      // data: '7830060',
      url: send_url,
      async: false,
      dataType: "jsonp",
      success: function (res) {
        //結果によって処理を振り分ける
        if (res.status == 200 && res.results !== null) {
          var result = res.results[0]
          //処理が成功したとき
          $('#not-find-toast').toast('hide')
          $('#id_address1').val(result.address1);
          $('#id_address2').val(result.address2);
          $('#id_address3').val(result.address3);
        } else {
          //エラーだった時
          $('#not-find-toast').toast('show')
          $('#id_address1').val("");
          $('#id_address2').val("");
          $('#id_address3').val("");
        }
      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {
        console.log(XMLHttpRequest);
      }
    });
  }
  
  
  
  