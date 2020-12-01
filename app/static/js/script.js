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