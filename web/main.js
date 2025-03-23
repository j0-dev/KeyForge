document.getElementById('_copy').addEventListener('click', async function(e){
    await navigator.clipboard.writeText(document.getElementById('_output').innerText);
})