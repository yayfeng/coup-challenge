from __future__ import division, print_function

from flask import request
from flask_restplus import Namespace, Resource, fields
from coup_challenge_app.logic.fleet_calculator import FleetCalculator

namespace = Namespace('fleet-management', 'Find number of Fleet Engineers')

response_model = namespace.model('ResponseModel', {
    'fleet_engineers': fields.Integer(
        description='Minimum number of FEs which are required to help the FM',
        required=True,
        example=3
    )
})


@namespace.route('')
class FleetManagementOps(Resource):
    post_request_model = namespace.model('PostRequestModel', {
        'scooters': fields.List(
            fields.Integer(
                description='Number of scooters for a district',
                required=True,
                min=0,
                max=1000,
                example=15
            ),
            description='List of number of scooters for districts in Berlin',
            example=[15, 10],
            min_items=1,
            max_items=100,
            required=True
        ),
        'C': fields.Integer(
            description="Number of scooters a single FM may supervise",
            required=True,
            min=1,
            max=999,
            example=12
        ),
        'P': fields.Integer(
            description="Number of scooters a single FE may supervise",
            required=True,
            min=1,
            max=1000,
            example=5
        ),
    })

    @namespace.expect(post_request_model)
    @namespace.marshal_with(response_model)
    def post(self):
        """
        Find number of Fleet Engineers
        """

        payload = request.json
        fc = FleetCalculator(
            payload['scooters'],
            payload['C'],
            payload['P']
        )

        return dict(fleet_engineers=fc.calculate())
