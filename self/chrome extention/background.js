chrome.commands.onCommand.addListener(function(command){
    chrome.storage.local.get("definedURL", function(result){
        if(result.definedURL != undefined){
            chrome.tabs.update({url:'http://'+result.definedURL});
            _gap.push(['_trackEvent', 'refresh', result.definedURL]);
    }else{
        chrome.tabs.update({url:'hppt://i.imgur.com/Jl1wSJi.jpg'});
    }
});
});