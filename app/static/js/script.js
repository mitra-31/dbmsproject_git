const imgDiv = document.querySelector('.profile');
const img = document.querySelector("#photo");
const file = document.querySelector('#file');
const uploadbtn = document.querySelector('#uploadbtn');

imgDiv.addEventListener('mouseenter',function()
{
    uploadbtn.style.display = "block";
});

imgDiv.addEventListener('mouseleave',function()
{
    uploadbtn.style.display = "none";
});


file.addEventListener('change',function(){
    const chooseFile = this.files[0];
    if(chooseFile){
        const reader = new FileReader();

        reader.addEventListener('load',function(){
            img.setAttribute('src',reader.result);
        });
        reader.readAsDataURL(chooseFile);
    }
})



audioPlayer();
    function audioPlayer() {
        var currentSong = 0;
        $("#player")[0].src = $("#playlist li a")[0];
        $("#player")[0].play();
        $("#playlist li a").click(function (e) {
            e.preventDefault();
            $("#player")[0].src = this;
            $("#player")[0].play();
            $("#playlist li").removeClass("current-song");
            currentSong = $(this).parent().index();
            $(this).parent().addClass("current-song");
        });
        $("#player")[0].addEventListener("ended", function () {
            currentSong++;
            if (currentSong == $("#playlist li a").length)
                currentSong = 0;
            $('#playlist li').removeClass("current-song");
        });
    }