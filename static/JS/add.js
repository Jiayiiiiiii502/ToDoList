// //日期选择器
//     $('#ddl').datetimepicker({
//         //'dddd YYYY年MM月DD日 HH:mm:ss' 星期几 年月日 时分秒
//         //YYYY年MM月DD日 HH:mm:ss' 年月日 时分秒
//         format: 'YYYY-MM-DD',
//         //国际化，这里指中文
//         language: "zh-CN",
//         //判断日期是否改变，改变就将日期选择框关闭
//     }).on('dp.change', function (ev) {
//         var newDateTime = ev.date ? ev.date.format('yyyy-MM-dd HH:mm:ss') : "";
//         var oldDateTime = ev.oldDate ? ev.oldDate.format('yyyy-MM-dd HH:mm:ss') : "";
//         if (newDateTime != oldDateTime) {
//             $(this).data("DateTimePicker").hide();
//         }
//     });