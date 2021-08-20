let produtos = [];
$('.add-cart').on('click', function(){
    let pk_cliente = $('#id-cliente').val();
    let pk_produto = $(this).val();
    let name_prod = $(this).attr('name');
    if (pk_cliente == '0'){
        Swal.fire({
            icon: 'warning',
            text: 'Selecione um cliente!',
            confirmButtonText: 'Fechar!',
            confirmButtonColor: '#30A5FF',
        })
    } else {
        $('.container-cart').attr('hidden', false);

        produtos.push($(this).val());

        const produtos_unique = new Set();
        produtos.forEach((prod) => {
            produtos_unique.add(prod);
        })
        create_cart(pk_produto, name_prod);

        let x = [...produtos_unique.values()]
    }
})

function create_cart(pk_produto, name_prod){
    let ok = true;
    $('.list-cart').each(function(){
        if (pk_produto == $(this).val()){
            ok = false
            Swal.fire({
            icon: 'info',
            text: 'Este produto já está no carrinho, caso queira mais de uma unidade, altere a quantidade!',
            confirmButtonText: 'Fechar!',
            confirmButtonColor: '#30A5FF',
            });
        };
    });
    if (ok){
        $('.cart').append(
        `<tr class="line" id_line="${pk_produto}">
            <td>
                <div class="button-group">
                    <button class="btn btn-danger btn-apagar list-cart btn-sm shadow list-cart" value="${pk_produto}">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </td>
            <td> ${name_prod} </td>
            <td><input type="tel" class="form-control qtd-item calc id-${pk_produto}" style="width:60px; height:30px" min="1" value="1"></td>
            <td><input type="tel" class="form-control price calc" id="id-${pk_produto}" style="width:100px; height:30px" min="1" value="1"></td>
            <td><span class="form-control total-item mult-total-${pk_produto}" style="width:100px; height:30px"></span></td>
        </tr>`);
    }
};

$(document).on('click', '.btn-apagar', function(){
    Swal.fire({
        icon: 'warning',
        showCloseButton: true,
        confirmButtonText: 'Sim',
        cancelButtonText: 'Fechar',
        confirmButtonColor: '#30A5FF',
        cancelButtonColor: '#F9243F',
        text: 'Tem certeza que deseja excluir o item?',
    }).then((result) => {
        if (result.isConfirmed) {
            $(this).parent().parent().parent().remove();
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'item excluido!',
                showConfirmButton: false,
                timer: 1500
            })
        };
        if ($('.cart').is(':empty')){
            $('.container-cart').attr('hidden', true);
        };
    })
});

let val_total = 0;
$('.btn-prosseguir').on('click', function(){
    let ok = true;
    let qtd_item = 0;
    let val_item = 0;
    val_total = 0;

    var select = document.querySelector('#id-cliente');
    var option = select.children[select.selectedIndex];
    var name_cliente = option.textContent;

    $('.qtd-item').each(function(){
        if ($(this).val() <= 0){
            ok = false;
            $(this).focus().css({'border-color': 'red', 'box-shadow': '0 0 0 0'});
            Swal.fire({
                position: 'center',
                icon: 'error',
                title: 'A quantidade precisa ser maior ou igual a 1!',
                showConfirmButton: false,
                timer: 3500
            })
        }else{
            qtd_item += parseInt($(this).val());
        }
    });
    if (ok){
        $('.price').each(function(){
            if($(this).val() == ''){
                ok = false;
                $(this).focus().css({'border-color': 'red', 'box-shadow': '0 0 0 0'});
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: 'Preencha o valor do(s) produto(s) para prosseguir!',
                    showConfirmButton: false,
                    timer: 3500
                })
            }
        });
    };

    if(ok){
        $('.total-item').each(function(){
            val_item = $(this).text().replace(',', '.');
            val_total += parseFloat(val_item);
        })
    };

    if (ok){
        modal_finalizar(name_cliente, qtd_item, val_total)
    }
});

function modal_finalizar(name_cliente, qtd_item, val_total){
    Swal.fire({
        position: 'center',
        title: 'Detalhes do pedido!',
        showCancelButton: true,
        confirmButtonText: 'Finalizar',
        cancelButtonText: 'Fechar',
        confirmButtonColor: '#30A5FF',
        cancelButtonColor: '#F9243F',
        html:`
            <div class="modal-body">
                <div class="row">
                    <div class="col-sm-6 col-md-8 col-lg-12">
                        <label for="cliente">Cliente: </label>
                        <span id="cliente"><h4>${name_cliente}</h4></span>

                        <label for="qtd">Quantidade de itens:</label>
                        <span id="qtd"><h4>${qtd_item}</h4></span>

                        <label for="valor">Valor total: </label>
                        <h3 class="text-success soma-total">${val_total.toFixed(2).replace('.',',')}</h4>
                        <br>
                        <label for="pgto">Forma de pagamento</label>
                        <select class="form-control pgto" name="pgto" id="pgto"><br>
                            <option value="0">---selecione---</option>
                            <option value="1">Dinheiro</option>
                            <option value="2">Débito</option>
                            <option value="3">Crédito</option>
                        </select>
                        <div class="pagamento">

                        </div>
                    </div>
                </div><br>
                <label for="obs">Observação</label>
                <textarea class="form-control" name="obs" id="obs" cols="auto" rows="auto" placeholder="Opcional"></textarea>
            </div>
        `
    }).then((result) =>{
        if(result.isConfirmed){
            create_json_cart()
        }
    })
}

$(document).on('change', '.pgto', function(){
    if ($(this).val() == '1'){
        var html = `
            <div class="row">
                <div class="col-sm-12">
                    <label for="cedulas">Valor pago</label>
                    <input type="tel" class="form-control cedulas" id="cedulas">
                    <div class="troco">
                    </div>
                </div>
            </div>
        `
        $('.pagamento').append(
            html
        )
    } else{
        $('.pagamento').empty();
    }
})

$(document).on('focusout', '.cedulas', function(){
    if($(this).val() != ''){
        $('.troco').empty().append('<label for="troco">Troco</label><span class="form-control text-warning" id="troco"></span>')
        calculo_troco();
    }
})

function calculo_troco(){
    let valor = $('#cedulas').val().replace(',', '.');
    let total = val_total;
    let prefix = 'R$: '
    if (valor){
        let troco = valor - total;
        $('#troco').append(prefix + troco.toFixed(2).replace('.', ','))
    }
}

$(document).on('focusout', '.calc', function(){
    let test = $(this).parent().parent().attr('id_line');
    let valor = $('#id-' + test).val().replace(',', '.');
    let qtd = $('.id-' + test).val();
    let total_por_item = parseInt(qtd) * parseFloat(valor).toFixed(2)

    if (valor && qtd != ''){
        $('.mult-total-' + test).empty().append(total_por_item.toFixed(2).replace('.', ','))
    }
});

var list_cart = [];
function create_json_cart(){
    var pedido = {'cliente': $('#id-cliente').val()}
    $('.line').each(function(){
        let pk_produto = $(this).attr('id_line');
        let qtd = $(this).children()[2].children[0].value;
        let valor_uni = $(this).children()[3].children[0].value;

        console.log(pk_produto)
        console.log(qtd)
        console.log(valor_uni)
        console.log('-----')
//        pedido['pedido'] = {
//            'id-produto': pk_produto,
//            'qtd': qtd,
//            'valor_uni': valor_uni
//        };
//        list_cart.push(pedido)
    });
//    console.log(list_cart)
}
