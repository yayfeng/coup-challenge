from __future__ import division, print_function

from flask_restplus import Namespace, Resource

namespace = Namespace('fleet-management', 'Find number of Fleet Engineers')


@namespace.route('')
class FleetManagementOps(Resource):
    def post(self):
        """
        Find number of Fleet Engineers
        """
        return "OK"
