import React from 'react'

const Persona = () => {
    let nome = 'Rachele';
    let cognome = 'Corsi';
    let nascita  = '05/03/1998';
    let luogo_nascita = 'Roma';
    let dati_anagrafici = ['Nome: ' + nome, 'Cognome: ' + cognome, 'Nato il: ' + nascita, 'Luogo di nascita ' + luogo_nascita];
    return (
        <div> 
            Persona
            {
                dati_anagrafici.map((d) => {
                    return <p>{d}</p>
                })
            }
        </div>
    )
}

export default Persona 

