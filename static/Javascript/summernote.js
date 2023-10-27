$('#content').summernote({
    placeholder: 'Write Post',
    tabsize: 2,
    minHeight: 150,
    toolbar: [
        ['style', ['style']],
        ['font', ['strikethrough', 'superscript', 'subscript']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video']],
        ['view', ['fullscreen', 'codeview', 'help']],
        ['height', ['height']]
    ],
    popover: {
        image: [
        ['image', ['resizeFull', 'resizeHalf', 'resizeQuarter', 'resizeNone']],
        ['float', ['floatLeft', 'floatRight', 'floatNone']],
        ['remove', ['removeMedia']]
        ],
        link: [
        ['link', ['linkDialogShow', 'unlink']]
        ],
        table: [
        ['add', ['addRowDown', 'addRowUp', 'addColLeft', 'addColRight']],
        ['delete', ['deleteRow', 'deleteCol', 'deleteTable']],
        ],
        air: [
        ['color', ['color']],
        ['font', ['bold', 'underline', 'clear']],
        ['para', ['ul', 'paragraph']],
        ['table', ['table']],
        ['insert', ['link', 'picture']]
        ]
    }

});


  function getCode(){
      var htmlContent = $('#summernote').summernote('code');
      console.log(htmlContent);
      return htmlContent
  }
