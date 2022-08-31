// csrf_tokenの取得
const parse_cookies = () => {
    let cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if (m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}

//フォーム送信時待機機能
const commonSynchronousRequest = (e) => {
    let url = e.target.getAttribute('url')
    let targetForm = e.target.getAttribute('targetForm')
    let method = e.target.getAttribute('method')
    let callback = e.target.getAttribute('callback')
    let formDatas = document.getElementById(targetForm);
    let mixedDatas = new FormData(formDatas);
    //トークンを取得
    let csrf_token = parse_cookies()
    // XHRの宣言
    let XHR = new XMLHttpRequest();
    XHR.open(method, url, true);
    XHR.setRequestHeader('X-CSRFToken', csrf_token)
    XHR.send(mixedDatas);
    XHR.onreadystatechange = () => {
        if (XHR.readyState == 4 && XHR.status == 200) {
            // console.log(XHR.responseText)
            console.log(callback)
            eval(callback)
        }
    };
}



