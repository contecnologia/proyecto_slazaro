tinymce.init({
    selector    : "textarea#id_contenido",
    content_css : "/static/css/tinymce.css",
    height      : 480,
    width       : 755,
    language    : "es",
    // toolbar     : "undo redo | styleselect | bold italic | link image"
    theme       : "modern",
    plugins     : [
        "advlist autolink lists link image charmap print preview hr anchor pagebreak",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking save table contextmenu directionality",
        // "emoticons template paste textcolor moxiemanager"
        "emoticons, template paste textcolor"
    ],
    toolbar1    : "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    toolbar2: "print preview media | forecolor backcolor emoticons",
    mage_advtab : true,
    templates   : [
        {title: 'Test template 1', content: 'Test 1'},
        {title: 'Test template 2', content: 'Test 2'}
    ]
});