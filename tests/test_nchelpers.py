import pyclimate.nchelpers as nch

def test_nc_copy_global_atts(nc_3d, nc_3d_bare):
    nch.nc_copy_atts(nc_3d, nc_3d_bare)
    assert 'model_id' in nc_3d_bare.ncattrs()
    assert 'source'  in nc_3d_bare.ncattrs()

def test_nc_copy_var_atts(nc_3d, nc_3d_bare):
    nch.nc_copy_atts(nc_3d, nc_3d_bare, 'tasmax', 'dummy_var')
    assert nc_3d_bare.variables['dummy_var'].standard_name == 'air_temperature'

def test_nc_get_360day_monthly_time_slices(nc_3d_360day):
    expected = [slice(i, i+30) for i in range(0, 360, 30)]
    slices = nch.get_monthly_time_slices(nc_3d_360day.variables['time'])
    assert slices  == expected
    for slice_ in slices:
        tasmax = nc_3d_360day.variables['tasmax']
        assert tasmax[slice_,:,:].shape == (30, 2, 2)

def test_nc_get_365day_monthly_time_slices(nc_3d_365day, days_365):
    d_paired = zip(days_365, days_365[1:])
    expected = [slice(x[0], x[1]) for x in d_paired]

    slices = nch.get_monthly_time_slices(nc_3d_365day.variables['time'])
    assert slices == expected

def test_nc_get_standard_monthly_time_slices(nc_3d_standard, days_leap):
    d_paired = zip(days_leap, days_leap[1:])
    expected = [slice(x[0], x[1]) for x in d_paired]

    slices = nch.get_monthly_time_slices(nc_3d_standard.variables['time'])
    assert slices == expected
