var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      myFunction(xhttp);
    }
};
xhttp.open("GET", "https://ra(word)githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Layout/T2P-layout-glyphs/ocr-p336.xml", true);
//xhttp.open("GET", "https://raw.githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Layout/T2P-layout/layout-p336.xml",true);
xhttp.send();

function myFunction(xml) {
    var response = xml["response"];
    parser = new DOMParser();
    xmlDoc = parser.parseFromString(response,"text/xml");

    imgpath = "https://raw.githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Pages/p336.png";
    imgdiv = document.querySelector('#imagePage');
    imgdiv.src=imgpath;
    originalSize=[imgdiv.width,imgdiv.height];
    imgdiv.style.width="100%";
    imgdiv.style.height="auto";
    reduction=parseInt(originalSize[0])/parseInt(imgdiv.offsetWidth);

    layoutdiv = document.querySelector('#layoutPage');
    /*
    tRs=xmlDoc.getElementsByTagName("TextRegion");
    for (i =0; i < tRs.length; i++){
      if (tRs[i].getAttribute("type")=="paragraph"){
        var p = document.createElement('p');
        p.className = tRs[i].getAttribute("type");
        p.id = tRs[i].getAttribute("id");
        p.appendChild(tRs[i].getElementsByTagName("Coords")[0]);
      }
      layoutdiv.appendChild(p);
      /*
      tLs = xmlDoc.getElementsByTagName("TextLine");
      for (j = 0;j<tLs.length;j++){
        var tL = document.createElement('div');
        tL.className = tLs[j].getAttribute("type");
        tL.id = tLs[j].getAttribute("id");
        tL.appendChild(tLs[j].getElementsByTagName("Coords")[0]);
        p.appendChild(tL);
        ws = xmlDoc.getElementsByTagName("Word");
        for (k = 0;k<ws.length;k++){
          var word = document.createElement('div');
          word.className = ws[k].getAttribute("type");
          word.id = ws[k].getAttribute("id");
          word.appendChild(ws[k].getElementsByTagName("Coords")[0]);
          tL.appendChild(word);
        }
      }
    }


    layoutElements=layoutdiv.childNodes;
    console.log(layoutElements);
    for (i=0; i < layoutElements.length ; i++){
      element = layoutElements[i];
      console.log(element.id);

      coords = element.getElementsByTagName("Coords")[0].getAttribute("points");
      coords = coords.split(' ');

      for (l in coords){
        list=coords[l].split(',');
        for(c in list){
          list[c][0]=parseInt(c[0]);
          list[c][1]=parseInt(c[1]);
        }
        coords[l]=list
      }

      //coordCrop=[coords.sort(sortFunctionXc).sort(sortFunctionYc)[0],coords.reverse()[0]]
      coordCrop=[coords.sort(sortFunctionXY)[0],coords.reverse()[0]];

      wDiv=(coordCrop[1][0]-coordCrop[0][0])/reduction;
      hDiv=(coordCrop[1][1]-coordCrop[0][1])/reduction;
      xDiv=(coordCrop[0][0]/reduction);
      yDiv=coordCrop[0][1]/reduction;

      element.style.left=String(xDiv+"px");
      element.style.top=String(yDiv+"px");
      element.style.width=String(wDiv+"px");
      element.style.height=String(hDiv+"px");

    }


    //console.log(xmlDoc)
    //console.log(document.getElementById("demo").innerHTML = xmlDoc.getElementsByTagName("Created")[0].firstChild.data);
}

function sortFunctionXc(a, b) {
    if (a[0] === b[0]) {
        return 0;
    }
    else {
        return (a[0] < b[0]) ? -1 : 1;
    }
}
function sortFunctionYc(a, b) {
    if (a[1] === b[1]) {
        return 0;
    }
    else {
        return (a[1] < b[1]) ? -1 : 1;
    }
}

function sortFunctionXY(a,b){
  return (a[0]-b[0])+(a[1]-b[1]);
}

function sortFunctionXY2(a,b){
  var i = 0;
  if (a[0]<b[0]){
    i+=1;
  }
  if (a[0]>b[0]){
    i-=1;
  }
  if (a[1]<b[1]){
    i+=1;
  }
  if (a[1]>b[1]){
    i-=1;
  }
  return i;
  */
}
