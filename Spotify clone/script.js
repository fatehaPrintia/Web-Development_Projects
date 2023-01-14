console.log("welcome to spotify");
let songIndex= 0;
let audioElement= new Audio('songs/1.mp3');
let masterPlay=document.getElementById('masterPlay');
let myProgressBar =document.getElementById('myProgressBar');
let gif =document.getElementById('gif');
let masterSongName =document.getElementById('masterSongName');
let songItems = Array.from(document.getElementsByClassName("songItem"));

let songs=[
    {songName:'Ghodey Pe Sawaar Qala ',filePath:'songs/Ghodey Pe Sawaar Qala .mp3',coverPath:'covers/1.jpg'},
    {songName:'Ek Din Ap',filePath:'songs/Ek Din Ap.mp3',coverPath:'covers/3.jpg'},
    {songName:'Chiltey Rod',filePath:'songs/Chiltey Rod.mp3',coverPath:'covers/4.jpg'},
    {songName:'Alag asmaaan',filePath:'songs/Alag asmaaan.mp3',coverPath:'covers/6.jpg'},
    {songName:'Tum Tak',filePath:'songs/Tum Tak.mp3',coverPath:'covers/7.jpg'},
    {songName:'Teri Jhuki Nazar',filePath:'songs/Teri Jhuki Nazar.mp3',coverPath:'covers/9.jpg'},
]

songItems.forEach((element,i) => {
   
    element.getElementsByTagName("img")[0].src=songs[i].coverPath;
    element.getElementsByClassName("songName")[0].innerText=songs[i].songName;   
});

//audioElement.play();
masterPlay.addEventListener('click',()=>{
    if(audioElement.paused || audioElement.currentTime <=0){
        audioElement.play();
       
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        gif.style.opacity= 1;
        
      
    }
    else{
       audioElement.pause();
       masterPlay.classList.remove('fa-pause-circle');
       masterPlay.classList.add('fa-play-circle');
       gif.style.opacity=0; 
       
    }
})
//Listen to event
audioElement.addEventListener('timeupdate',()=>{
    console.log('timeupdate');
    progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    myProgressBar.value=progress;
})




myProgressBar.addEventListener("change",()=>{
    audioElement.currentTime= myProgressBar.value*audioElement.duration/100 ;
})


const makeAllPlayes=()=>{
  
    Array.from(document.getElementsByClassName('songsItemPlay')).forEach((element)=>{
        element.classList.remove('fa-pause-circle');
        element.classList.add('fa-play-circle');
    })

}




Array.from(document.getElementsByClassName('songsItemPlay')).forEach((element)=>{
        element.addEventListener('click',(e)=>{
            songIndex=parseInt(e.target.id); 
            console.log(songIndex);
        if (audioElement.paused){
            
        makeAllPlayes();   
        songIndex=parseInt(e.target.id); 
        console.log(songIndex);
        e.target.classList.remove('fa-play-circle');
        e.target.classList.add('fa-pause-circle');
        audioElement.src=`songs/${songIndex}.mp3`;
        masterSongName.innerText='';
        masterSongName.innerText=songs[songIndex-1].songName;
        audioElement.currentTime=0;
        audioElement.play();
        gif.style.opacity=1;
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');


        }
        else{
          
        songIndex=parseInt(e.target.id); 
        e.target.classList.add('fa-play-circle');
        e.target.classList.remove('fa-pause-circle');
        audioElement.currentTime=0;
        audioElement.pause();
        gif.style.opacity=0;
        masterPlay.classList.add('fa-play-circle');
        masterPlay.classList.remove('fa-pause-circle');

        }
        

    })
})

document.getElementById('next').addEventListener('click',()=>{
    if(songIndex>=6){
        songIndex=1;
    }
    else{
        songIndex+=1;

    }
    masterSongName.innerText='';
    audioElement.src=`songs/${songIndex}.mp3`;
    masterSongName.innerText=songs[songIndex-1].songName;
        audioElement.currentTime=0;
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
    
})


document.getElementById('previous').addEventListener('click',()=>{
    if(songIndex<2){
        songIndex=6;
    }
    else{
        songIndex-=1;

    }
    masterSongName.innerText='';
    audioElement.src=`songs/${songIndex}.mp3`;
    masterSongName.innerText=songs[songIndex-1].songName;
        audioElement.currentTime=0;
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
    
})
