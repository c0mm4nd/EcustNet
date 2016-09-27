// cordovaHTTP Version
// function httpGet(url, success, fail){
//   cordovaHTTP.get(url, {}, {}, success, fail);
// }

// Jquery Version
var request = require('request');
var cheerio = require("cheerio");
stuID = 10142045; // 你的学号
stuPW = 10142045; // 你的密码
// console.log(request);
function httpGet(url, success, fail){
  data={};
  // console.log(request);
  // if
  request(url, function (error, response, body) {
    var res = {};
    res.data = body;
    res.header = response;
    if (!error && response.statusCode == 200) {
      success(res);
    }else{
      fail(res);
    }
  });
}

function httpPost(url, data, success, fail){
  form={"form": data};
  // console.log(request);
  // if
  request.post(url, form, function (error, response, body) {
    var res = {};
    res.data = body;
    res.header = response;
    if (!error && response.statusCode == 200) {
      success(res);
    }else{
      fail(res);
    }
  });
}

function validReqSuccess(res){
  console.log(res.data);
  if (res.data.indexOf("http-equiv='refresh'")>0){
    httpGet("http://login.ecust.edu.cn", firstReqSuccess, firstReqFail);
  }else{
    console.log("already Login");
  }
}

function validReqFail(res){
  console.log("validReqFail");
}

function firstReqSuccess(res){
  console.log("firstReqSuccess");
  // console.log(res.data);
  var reg = /http:\/\/login.ecust.edu.cn\/&arubalp=.*\'/;
  rst = reg.exec(res.data);
  // console.log(rst[0]);
  // console.log(rst[0].substring(-1,rst[0].length-1));
  secondUrl = rst[0].substring(-1,rst[0].length-1)
  httpGet(secondUrl, secondReqSuccess, secondReqFail);
}

function firstReqFail(res){
  console.log("firstReqFail");
}

function secondReqSuccess(res){
  console.log("secondReqSuccess");
  // console.log(res.data);
  console.log("Header is :");
  console.log(res.header.req._header); //need to change
  acIdReg = /\/index_([\d]+).html/
  acId = acIdReg.exec(res.header.req._header)[0].substring(7,8);
  // console.log(acId);
  argsReg= /cmd.+cn%2F/ //cmd=login&switchip=192.168.71.4&mac=34:de:1a:1e:f9:15&ip=172.21.178.43&essid=ECUST&apname=FX-HDZX-2F-W01&apgroup=fx-free-apgroup&url=http%3A%2F%2Flogin%2Eecust%2Eedu%2Ecn%2F
  args = argsReg.exec(res.header.req._header)[0]
  // console.log(args);
  // locationReg = /http:\/\/[0-9]*.[0-9]*.[0-9]*.[0-9]*\//;
  // location = locationReg.exec()
  locationReg = /host:\s[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*/;
  location = "http://" + locationReg.exec(res.header.req._header)[0].substring(6) + "/";
  // console.log(location);
  thirdUrl =location + "ac_detect.php?" + "ac_id="+ acId + "&" + args;
  // console.log(thirdUrl);
  httpGet(thirdUrl, thirdReqSuccess, thirdReqFail);
}

function thirdReqFail(res){
  console.log("thirdReqFail");
}

function thirdReqSuccess(res){
  console.log("thirdReqSuccess");
  console.log(res.header.request.redirects);//path redirects
  for (var p in res.header.request._redirect.redirects){ console.log(p);}
  finalUrl = res.header.request._redirect.redirects[0].redirectUri;
  console.log(finalUrl);
  html = res.data;
  // console.log(html);
  var $ = cheerio.load(html);
  data = {};
  data["action"] = $("input[name='action']").val();
  data["ac_id"] = $("input[name='ac_id']").val();
  data["user_ip"] = $("input[name='user_ip']").val();
  data["nas_ip"] = $("input[name='nas_ip']").val();
  data["user_mac"] = $("input[name='user_mac']").val();
  data["url"] = $("input[name='url']").val();
  data["ip"] = $("input[name='ip']").val();
  data["username"] = stuID + "@free";
  data["password"] = stuPW;
  data["ajax"] = "1" ;
  httpPost(finalUrl, data, finalReqSuccess, finalReqFail);
}

function finalReqFail(res){
  console.log("finalReqFail");
}

function finalReqSuccess(res){
  console.log("finalReqSuccess");
}

function secondReqFail(res){
  console.log("secondReqFail");
}

httpGet("http://www.baidu.com", validReqSuccess, validReqFail);
