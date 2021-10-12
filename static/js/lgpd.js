let lgpdUrl = 'http://127.0.0.1:8000/';

let lgpdHtml = `
    <div class="lgpd" class="fixed">
        <div class="lgpd--left">
            Utilizamos cookies essenciais para melhor expriência do usuário,  
            para conferir detalhadamente leia nossa <b> <a href="http://127.0.0.1:8000/politPriv/">Política de Privacidade</a></b>. <br>
            Ao continuar navegando, você declara estar ciente dessas condições.
        </div>
        <div class="lgpd--right">
            <button>ok</button>
        </div>
    </div>
    
`;

let lsContent = localStorage.getItem('lgpd');

if(!lsContent){
    document.body.innerHTML += lgpdHtml;

    let lgpdArea = document.querySelector('.lgpd');
    let lgpdButton = lgpdArea.querySelector('button');

    lgpdButton.addEventListener('click', async () => {
        lgpdArea.remove();

        let result = await fetch(lgpdUrl);
        let json = await result.jason();

        if(json.error != ''){
            let id = json.id;
            localStorage.setItem('lgpd', id);
        }

        
    });
}