$('.btn-trash').on({
    'click': function () {
        let pk = $(this).val();
        Swal.fire({
            title: 'ATENÇÃO',
            text: "Tem Certeza que deseja excluir?",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'SIM',
            cancelButtonText: 'NÃO'
        }).then((result) => {
            if (result.value) {
                $.ajax({
                    'url': '/user/delete-user/',
                    'method': 'POST',
                    'dataType': 'json',
                    'data': {
                        'pk': pk
                    },
                    success: function (data) {
                        if (data.success) {
                            Swal.fire({
                                title: 'Excluido!',
                                text: "O usuário foi excluido!",
                                icon: 'success',
                                allowOutsideClick: false,
                                allowEscapeKey: false,
                            }).then((result) => {
                                if (result.value) {
                                    location.reload();
                                }
                            })
                        } else {
                            Swal.fire(
                                'Erro!',
                                'Erro ao tentar excluir o usuário!',
                                'error'
                            )
                        }
                    }
                })
            }
        })
    }
})