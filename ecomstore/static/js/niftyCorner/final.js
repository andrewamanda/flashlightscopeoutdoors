window.onload=function(){
if(!NiftyCheck())
    return;
RoundedTop("div.leftnav_innercontainer","#e2e2e2","#F5C66C");
RoundedBottom("div.bottom_padding","#e2e2e2","#FFF");
RoundedBottomIfDisplay("div#ShopByCategory","div#leftnav_catalog","#e2e2e2","#F5C66C");
RoundedBottomIfDisplay("div#ShopByBrand","div#leftnav_brand","#e2e2e2","#F5C66C");
RoundedBottomIfDisplay("div#ShopByPrice","div#leftnav_price","#e2e2e2","#F5C66C");
RoundedBottomIfDisplay("div#ShopByBrightness","div#leftnav_brightness","#e2e2e2","#F5C66C");


}