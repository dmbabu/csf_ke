
//Check minimum leave application days
// frappe.ui.form.on('Leave Application',  {
//     validate: function(frm) {
//         minimum_days = frm.doc.custom_minimum_leave_application_days;
//         days_to_leave = frappe.datetime.get_diff(frm.doc.from_date, frm.doc.posting_date);
        
//         if (days_to_leave < minimum_days) {
//             frappe.msgprint({
//                 title: __('Error'), 
//                 indicator: 'red', 
//                 message: __('Your leave application is ' + days_to_leave + ' days to the leave day. Application must be made at least ' + minimum_days + ' days before the leave date.')
//             });
//             frappe.validated = false;
//         }
//     }
// });