<?php
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
$content = htmlentities($xmlfile);
if (strlen($xmlfile)>0) {
    if (strpos($content,"!ENTITY") || strpos($content,"!DOCTYPE") || strpos($content,"!ELEMENT") || strpos($content,".dtd") || strpos($content,"file://") ||  strpos($content,".php") ){
        echo "<br><p style='color: red;'>Malicious payload has been detected!</p>";
    }else {
        $dom = new DOMDocument();
        $dom->loadXML($xmlfile, LIBXML_NOENT);
        $info = simplexml_import_dom($dom);
        echo "<br><p style='color: black;'>your message has been sent</p>";
    }
}else {
    echo "Nope";
}
?>