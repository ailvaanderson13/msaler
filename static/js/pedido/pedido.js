function mask_(){
    $('.price').mask('000.000.000.000.000,00', {reverse: true});
}
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
        var html = `
            <tr>
                <td>
                    <div class="button-group">
                        <button class="btn btn-danger btn-apagar list-cart" btn-sm shadow list-cart" value="${pk_produto}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </td>
                <td> ${name_prod} </td>
                <td><input type="tel" class="form-control qtd-item" style="width:60px; height:30px" min="1" value="1"></td>
                <td><input type="tel" class="form-control price" style="width:100px; height:30px" min="1"></td>
            </tr>
        `
        $('.cart').append(
            html
        );
        mask_();
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

$('.btn-prosseguir').on('click', function(){
    let ok = true;
    let dict_cart = {};
    let qtd_item = 0;
    let val_item = 0;

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
    console.log(qtd_item)
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
            } else {
                val_item += parseFloat($(this).val());
            }
        });
    }
    console.log(val_item)

    if (ok){
        modal_finalizar(name_cliente, qtd_item)
    }
});

function modal_finalizar(name_cliente, qtd_item){
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
                        <span id="valor"><h4 class="text-success"><strong>R$: 1200,00</strong></h4></span>
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
    })
}

$(document).on('change', '.pgto', function(){
    if ($(this).val() == '1'){
        var html = `
            <div class="row">
                <div class="col-sm-12">
                    <label for="cedulas">Valor pago</label>
                    <input type="tel" class="form-control cedulas price" id="cedulas">
                    <div class="troco">
                    </div>
                </div>
            </div>
        `
        $('.pagamento').append(
            html
        )
        mask_();
    } else{
        $('.pagamento').empty();
    }
})

$(document).on('focusout', '.cedulas', function(){
    if($(this).val() != ''){
        $('.troco').empty().append('<label for="troco">Troco</label><input class="form-control" id="troco" value="aqui" disabled>')
    }
})

