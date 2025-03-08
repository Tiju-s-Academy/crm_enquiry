from odoo.http import Controller, request, route

class WebFormController(Controller):
    @route('/thanks', auth='public', website=True)
    def helpdesk_request_web_form(self, **kwargs):
        return request.render('crm_enquiry.thank_you_template')

    @route('/course_enquiry', auth='public', website=True)
    def create_enquiry2(self):
        category = request.env['product.category'].sudo().search([
            ('name', 'not in', ['All', 'Deliveries','Expenses','Saleable','Courses','Events','DM','Hostel','NC'])
        ])
        values = {
            'category': category,
        }
        return request.render('crm_enquiry.course_enquiry_form_template', values)

    @route('/course_enquiry/submit', type='http', auth='public', website=True,
           methods=['POST'])
    def web_form_submit2(self, **post):
        customer_name = post.get('customer_name')
        phone = post.get('phone_number')
        email = post.get('email')
        category_id = post.get('category_id')
        team = request.env['crm.team'].sudo().search([('name', '=', 'Sales Team Mavelikkara')], limit=1)


        source = request.env['utm.source'].sudo().search([('name', '=', 'ManyChat')], limit=1)
        if not source:
            source = request.env['utm.source'].sudo().create({'name': 'ManyChat'})

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
            'categ_id': category_id,
            'team_id': team.id if team else False,
            'expected_revenue': 0,
            'source_id': source.id,
            'type': 'lead',
        })

        return request.redirect('/thanks')

    @route('/course_details', auth='public', website=True)
    def create_enquiry(self):
        category = request.env['product.category'].sudo().search([
            ('name', 'not in', ['All', 'Deliveries','Expenses','Saleable','Courses','Events','DM','Hostel','NC'])
        ])
        values = {
            'category': category,
        }
        return request.render('crm_enquiry.course_details_form_template', values)

    @route('/course_details/submit', type='http', auth='public', website=True,
           methods=['POST'])
    def web_form_submit(self, **post):
        customer_name = post.get('customer_name')
        phone = post.get('phone_number')
        email = post.get('email')
        category_id = post.get('category_id')
        team = request.env['crm.team'].sudo().search([('name', '=', 'Sales Team Mavelikkara')], limit=1)

        source = request.env['utm.source'].sudo().search([('name', '=', 'Google Ads')], limit=1)
        if not source:
            source = request.env['utm.source'].sudo().create({'name': 'Google Ads'})

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
            'categ_id': category_id,
            'team_id': team.id if team else False,
            'source_id': source.id,
            'expected_revenue': 0,
            'type': 'lead',
        })

        return request.redirect('/thanks')