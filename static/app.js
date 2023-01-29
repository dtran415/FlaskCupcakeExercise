async function showCupcakes() {
    const response = await axios.get('http://localhost:5000/api/cupcakes');

    const list = $('#cupcakes-list')
    list.empty()
    for (let cupcake of response.data.cupcakes) {
        list.append(generateCupcakeHTML(cupcake))
    }
}

function generateCupcakeHTML(cupcake) {
    return $('<li>').append([$('<img>',{'src':`${cupcake.image}`}), $('<br>'), $('<span>').text(`${cupcake.flavor}|${cupcake.size}|${cupcake.rating}`)])
}

async function createCupcake(e) {
    e.preventDefault()
    const flavor = $('#flavor').val()
    const rating = $('#rating').val()
    const size = $('#size').val()
    const image = $('#image').val()
    const response = await axios.post('http://localhost:5000/api/cupcakes', {flavor, rating, size, image})
    showCupcakes()
    $('#cupcake-form').trigger('reset')
}

$(function(){
    console.log("starting")
    showCupcakes()
    $('#cupcake-form').on('submit', createCupcake)
})