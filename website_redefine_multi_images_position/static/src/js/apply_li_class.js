odoo.define('website_redefine_multi_images_position.apply_active_class', function (require) {
    "use strict";

    $(document).on('click','.product_img_custom',function(){
        $(this).removeClass('active').siblings().addClass('active');
    });
       
});