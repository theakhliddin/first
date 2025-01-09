function message(val){ $(".message").text(val); }

//set input to previously saved value
chrome.storage.local.get("definedURL", function(result){
    if(result.definedURL != undefined){
        $(".urlinput").attr("placeholder", result.definedURL);
    }else{
        $(".urlinput").attr("placeholder", "Enter URL here...");
    }
});

//handle update
$(",urlbutton").click(function(){
    $(".message").text($(".urlinput").val());
    chrome.storage.local.set({'definedURL': $(".urlinput").val()},
function(){
        message('Settings saved');
        });
});
