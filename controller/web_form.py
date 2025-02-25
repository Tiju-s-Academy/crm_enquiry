from odoo.http import Controller, request, route

class WebFormController(Controller):
    @route('/thanks', auth='public', website=True)
    def helpdesk_request_web_form(self, **kwargs):
        return request.render('crm_enquiry.thank_you_template')

    @route('/course_enquiry', auth='public', website=True)
    def create_enquiry(self):
        course = request.env['product.product'].sudo().search([])
        values = {
            'course': course,
        }
        return request.render('crm_enquiry.course_enquiry_form_template', values)

    @route('/course_enquiry/submit', type='http', auth='public', website=True,
           methods=['POST'])
    def web_form_submit(self, **post):
        customer_name = post.get('customer_name')
        phone = post.get('phone_number')
        email = post.get('email')
        course_id = post.get('course_id')
        team = request.env['crm.team'].sudo().search([('name', '=', 'Sales Team Mavelikkara')], limit=1)
        course = request.env['product.product'].sudo().browse(int(course_id)) if course_id else False

        source = request.env['utm.source'].sudo().search([('name', '=', 'Many2Chat')], limit=1)
        if not source:
            source = request.env['utm.source'].sudo().create({'name': 'Many2Chat'})

        partner = request.env['res.partner'].sudo().create({
            'name': customer_name,
            'phone': phone,
            'email': email,
        })

        crm_lead = request.env['crm.lead'].sudo().create({
            'name': f'Course Enquiry - {customer_name}',
            'partner_id': partner.id,
            'phone': phone,
            'email_from': email,
            'user_id': False,
            'course_id': course.id if course else False,
            'team_id': team.id if team else False,
            'expected_revenue': course.lst_price if course else 0,
            'source_id': source.id,
            'type': 'lead',
        })

        return request.redirect('/thanks')