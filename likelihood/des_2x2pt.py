from cobaya.likelihoods.des_y3._cosmolike_prototype_base import _cosmolike_prototype_base
import cosmolike_des_y3_interface as ci

class des_2x2pt(_cosmolike_prototype_base):
	# ------------------------------------------------------------------------
	# ------------------------------------------------------------------------
	# ------------------------------------------------------------------------

	def initialize(self):
		super(des_2x2pt,self).initialize(probe="2x2pt")

	# ------------------------------------------------------------------------
	# ------------------------------------------------------------------------
	# ------------------------------------------------------------------------

	def logp(self, **params_values):
		self.set_cosmo_related()

		self.set_lens_related(**params_values)

		self.set_source_related(**params_values)

		datavector = ci.compute_data_vector()

		return self.compute_logp(datavector)

