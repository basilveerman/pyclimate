import warnings

import numpy as np
from netCDF4 import Dataset

from pyclimate import Cmip5File

class DerivableBase(object):
    required_atts = ['model', 'experiment', 'run', 't_start', 't_end']

    def __init__(self, **kwargs):
        for att in required_meta:
            try:
                v = kwargs.pop(att)
                setattr(self, att, v)
            except KeyError:
                raise KeyError('Required attribute {} not provided'.format(att))
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        self.variables = {}

    def add_base_variable(self, variable, dataset_fp):
        self.variables[variable] = dataset_fp

class DerivedVariable(object):
    variable_name = ''
    required_vars = []

    def __init__(self, model_set, outdir):
        self.model_set = model_set
        self.outdir = outdir

    def has_required_vars(self, required_vars):
        if not all([x in self.model_set.keys() for x in required_vars]):
            warnings.warn('Insufficient base variables to calculate {}'.format(self.variable_name))
            return False
        return True

    def get_output_file_path(self, basevar):
        cf = Cmip5File(self.model_set[basevar])
        cf.variable = self.variable_name
        cf.root = self.outdir
        return cf.fullpath

class tas(DerivedVariable):
    variable_name = 'tas'
    required_vars = ['tasmax', 'tasmin']

    def __call__(self):
        if not self.has_required_vars(required_vars):
            return 1

        outfp = get_output_file_path_from_base(required_vars[0])
        self.setup(outfp)

        nc_tasmax = Dataset(self.model_set['tasmax'])
        nc_tasmin = Dataset(self.model_set['tasmin'])

        ncvar_tas[i,:,:] = (var_tasmax[i,:,:] + var_tasmin[i,:,:]) / 2

    def setup(nc_base, outfp):
        cf = Cmip5File(outfp)

        if not os.path.exists(cf.dirname):
            os.makedirs(cf.dirname)

        nc = Dataset(outfp, 'w')
        ncvar = nc_copy_var(nc_source, nc, 'tasmax', 'tas', copy_attrs=True, copy_data=False)
        nc_copy_atts(nc_source, nc) #copy global atts
        ncvar.long_name = 'Near-Surface Air Temperature'
        ncvar.standard_name = 'air_temperature'
        ncvar.units = 'K'
        ncvar.cell_methods = 'time: mean'
        ncvar.cell_measures = 'area: areacella'

        return nc, ncvar

class gdd(object):
    def __call__():
        pass

# def setup_gdd(nc_source, d, outdir):

#     gdd = Cmip5File(**d)
#     gdd.variable = 'gdd'
#     gdd.root = outdir
#     if not os.path.exists(gdd.dirname):
#         os.makedirs(gdd.dirname)

#     nc = Dataset(gdd.fullpath, 'w')
#     ncvar = nc_copy_var(nc_source, nc, 'tasmax', 'gdd', copy_data=False)
#     nc_copy_atts(nc_source, nc) #copy global atts
#     ncvar.units = 'degree days'
#     ncvar.long_name = 'Growing Degree Days'

    # return nc, ncvar

class hdd(object):
    def __call__():
        pass

# def setup_hdd(nc_source, d, outdir):

#     hdd = Cmip5File(**d)
#     hdd.variable = 'hdd'
#     hdd.root = outdir
#     if not os.path.exists(hdd.dirname):
#         os.makedirs(hdd.dirname)

#     nc = Dataset(hdd.fullpath, 'w')
#     ncvar = nc_copy_var(nc_source, nc, 'tasmax', 'hdd', copy_data=False)
#     nc_copy_atts(nc_source, nc) #copy global atts
#     ncvar.units = 'degree days'
#     ncvar.long_name = 'Heating Degree Days'

#     return nc, ncvar


class ffd(object):
    def __call__():
        pass

# def setup_ffd(nc_source, d, outdir):

#     ffd = Cmip5File(**d)
#     ffd.variable = 'ffd'
#     ffd.root = outdir
#     if not os.path.exists(ffd.dirname):
#         os.makedirs(ffd.dirname)

#     nc = Dataset(ffd.fullpath, 'w')
#     ncvar = nc_copy_var(nc_source, nc, 'tasmax', 'ffd', copy_data=False)
#     nc_copy_atts(nc_source, nc) #copy global atts
#     ncvar.units = 'days'
#     ncvar.long_name = 'Frost Free Days'

#     return nc, ncvar

class pas(object):
    def __call__():
        pass

# def setup_pas(nc_source, d, outdir):

#     pas = Cmip5File(**d)
#     pas.variable = 'pas'
#     pas.root = outdir
#     if not os.path.exists(pas.dirname):
#         os.makedirs(pas.dirname)

#     nc = Dataset(pas.fullpath, 'w')
#     ncvar = nc_copy_var(nc_source, nc, 'pr', 'pas', copy_data=False)
#     nc_copy_atts(nc_source, nc) #copy global atts
#     ncvar.units = 'days'
#     ncvar.long_name = 'Frost Free Days'

#     return nc, ncvar
