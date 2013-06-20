/**
 * Created with PyCharm.
 * User: macbookair
 * Date: 6/20/13
 * Time: 1:26 AM
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){
    $('#geotrigger').hide();

    $(document).on('click', '#triggertype', function(){
        $triggertype = $('input:radio[name=triggertype]:checked').val();
        if($triggertype === "timetrigger"){
            $('#geotrigger').hide();
            $('#timetrigger').show();
        }
        else if($triggertype === "geotrigger")
        {
            $('#geotrigger').show();
            $('#timetrigger').hide();
        }
    });
});