var page= 350;
var originalSize=[];
var reduction;

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      functXML(xhttp);
    }
};
//xhttp.open("GET", "https://raw.githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Layout/T2P-layout-glyphs/ocr-p336.xml", true);
xhttp.open("GET", "/Layout/T2P-layout-glyphs/ocr-p"+page+".xml", true);
xhttp.send();

function checkImage(self){
  var div = self.value;
  if(self.checked){
    document.querySelector("#"+div).style.display="block";
  }else{
    document.querySelector("#"+div).style.display="none";
  }
}
function checkBorders(self){
  var divs = document.querySelectorAll("."+self.value);
  var len=divs.length
  if(self.checked){
    for(i=0 ; i<len ; i++){
      divs[i].style.borderStyle="solid";
    }
  }else{
    for(i=0 ; i<len ; i++){
      divs[i].style.borderStyle="none";
    }
  }
}




function functXML(xml) {
  var response = xml["response"];
  parser = new DOMParser();
  xmlDoc = parser.parseFromString(response,"text/xml");

  //imgpath = "https://raw.githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Pages/p336.png";
  imgpath="/Pages/"+xmlDoc.querySelector("Page").getAttribute("imageFilename");
  imgdiv = document.querySelector('#imagePage');
  imgdiv.src=imgpath;

  imgdiv.onload = function(){

    originalSize=[imgdiv.width,imgdiv.height];
    imgdiv.style.width="100%";
    imgdiv.style.height="auto";
    reduction=parseInt(originalSize[0])/parseInt(imgdiv.offsetWidth);

    layoutdiv = document.querySelector('#layoutPage');

    tRs=xmlDoc.getElementsByTagName("TextRegion");

    for (i =0, iLen=tRs.length ; i < iLen ; i++){
      tR = xml2html(layoutdiv,tRs[i]);

      tLs = tRs[i].getElementsByTagName("TextLine");
      for (j = 0, jLen=tLs.length ; j < jLen ; j++){
        tL = xml2html(tR,tLs[j])

        words = tLs[j].getElementsByTagName("Word");
        for (k = 0, kLen=words.length ; k < kLen ; k++){
          word = xml2html(tL,words[k])

          glyphs = words[k].getElementsByTagName("Glyph");
          for (l = 0,lLen=glyphs.length;l<lLen;l++){
            glyph = xml2html(word,glyphs[l])
          }
        }
      }
    }

    layoutElements=layoutdiv.querySelectorAll("div");
    //console.log(layoutElements);
    for (i=0; i < layoutElements.length ; i++){
      var element = layoutElements[i];

      offsetCoords=coords2offset(element);
      element.style.left=String(offsetCoords[0]+"px");
      element.style.top=String(offsetCoords[1]+"px");
      element.style.width=String(offsetCoords[2]+"px");
      element.style.height=String(offsetCoords[3]+"px");

    }
  }
}

function sortFunctionXY(a,b){
  return (a[0]-b[0])+(a[1]-b[1]);
}

function xml2html(parentNode,xmlelement){
  var div = document.createElement('div');
  div.className = xmlelement.tagName;
  div.id = xmlelement.getAttribute("id");

  textEquivS=xmlelement.getElementsByTagName("Unicode")
  textEquiv= textEquivS[textEquivS.length-1].textContent;
  div.textContent=textEquiv;

  if(xmlelement.getElementsByTagName("Coords")[0]!=undefined){
    div.appendChild(xmlelement.getElementsByTagName("Coords")[0]);
  }

  parentNode.appendChild(div);
  return(div);
}


function coords2offset(element){
  if (element.getElementsByTagName("Coords")[0]!=undefined){
    coords = element.getElementsByTagName("Coords")[0].getAttribute("points");
  }else{
    coords= "0,0 0,0"
  }

  coords = coords.split(' ');

  for (l in coords){
    list=coords[l].split(',');
    for(c in list){
      list[c][0]=parseInt(c[0]);
      list[c][1]=parseInt(c[1]);
    }
    coords[l]=list
  }

  coordCrop=[coords.sort(sortFunctionXY)[0],coords.reverse()[0]];

  wDiv=(coordCrop[1][0]-coordCrop[0][0])/reduction;
  hDiv=(coordCrop[1][1]-coordCrop[0][1])/reduction;

  xDiv=(coordCrop[0][0]/reduction);
  yDiv=(coordCrop[0][1]/reduction);

  var tmp=element;
  while(tmp.parentNode.id!="layoutPage"){
      tmp=tmp.parentNode;
      xDiv-=tmp.offsetLeft;
      yDiv-=tmp.offsetTop;
  }

  return(offsetCoords=[xDiv,yDiv,wDiv,hDiv])
}
