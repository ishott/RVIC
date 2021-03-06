"""
share.py
"""
import sys
from netCDF4 import default_fillvals
import time as time_mod
from getpass import getuser

# ----------------------- CONSTANTS --------------------------------- #
EARTHRADIUS = 6.37122e6  # meters
WATERDENSITY = 1000.

# area
METERSPERKM = 1000.
METERSPERMILE = 1609.34
METERS2PERACRE = 4046.856

# time
# reference time
REFERENCE_STRING = '0001-1-1 0:0:0'
REFERENCE_DATE = 10101                           # i.e. REFERENCE_STRING
REFERENCE_TIME = 0                               # i.e. REFERENCE_STRING
TIMEUNITS = 'days since ' + REFERENCE_STRING     # do not change (MUST BE DAYS)!
TIMESTAMPFORM = '%Y-%m-%d-%H'
CALENDAR = 'noleap'
HOURSPERDAY = 24.
SECSPERHOUR = 3600.
MINSPERHOUR = 60.
MINSPERDAY = HOURSPERDAY * MINSPERHOUR
SECSPERDAY = HOURSPERDAY * SECSPERHOUR

# length
MMPERMETER = 1000.
CMPERMETER = 100.

# precision
PRECISION = 1.0e-30
NC_DOUBLE = 'f8'
NC_FLOAT = 'f4'
NC_INT = 'i4'
NC_CHAR = 'S1'
MAX_NC_CHARS = 256

# fill values
FILLVALUE_F = default_fillvals[NC_DOUBLE]
FILLVALUE_I = default_fillvals[NC_INT]

# filenames
RPOINTER = 'rpointer'

# tracers
RVIC_TRACERS = ('LIQ',)

# Calendar key number for linking with CESM
CALENDAR_KEYS = {0:['None'],
                 1:['noleap', '365_day'],
                 2:['gregorian', 'standard'],
                 3:['proleptic_gregorian'],
                 4:['all_leap', '366_day'],
                 5:['360_day'],
                 6:['julian']}

# ----------------------- NETCDF VARIABLES --------------------------------- #
class NcGlobals:
    def __init__(self, title='',
                 casename='',
                 casestr='',
                 history='Created: {} by {}'.format(time_mod.ctime(time_mod.time()), getuser()),
                 institution='Univeristy of Washington', source=sys.argv[0],
                 references='Based on the initial model of Lohmann, et al., 1996, Tellus, 48(A), 708-721',
                 comment='Output from the RVIC Streamflow Routing Model.',
                 Conventions='CF-1.6',
                 RvicPourPointsFile='',
                 RvicFdrFile='',
                 RvicUHFile='',
                 RvicDomainFile=''):
        self.title = title
        self.casename = casename
        self.history = history
        self.institution = institution
        self.source = source
        self.references = references
        self.comment = comment
        self.Conventions = Conventions
        self.RvicPourPointsFile = RvicPourPointsFile
        self.RvicUHFile = RvicUHFile
        self.RvicFdrFile = RvicFdrFile
        self.RvicDomainFile = RvicDomainFile

    def update(self):
        self.history = 'Created: {}'.format(time_mod.ctime(time_mod.time()))


class NcVar:
    def __init__(self, long_name='', units=''):
        self.long_name = long_name
        self.units = units

# Coordinate Variables
time = NcVar(long_name='time',
             units=TIMEUNITS)

time_bnds = NcVar()

timesteps = NcVar(long_name='Series of timesteps',
                  units='unitless')

lon = NcVar(long_name='longitude',
            units='degrees_east')

lat = NcVar(long_name='latitude',
            units='degrees_north')

xc = NcVar(long_name='longitude',
           units='degrees_east')

yc = NcVar(long_name='latitude',
           units='degrees_north')

# Data Variables
fraction = NcVar(long_name='fraction of grid cell that is active',
                  units='unitless')

unit_hydrograph = NcVar(long_name='Unit Hydrograph',
                         units='unitless')

avg_velocity = NcVar(long_name='Flow Velocity Parameter',
                     units='m s-1')

avg_diffusion = NcVar(long_name='Diffusion Parameter',
                      units='m2 s-1')

global_basin_id = NcVar(long_name='Global Basin ID from RvicFdrFile',
                        units='unitless')

full_time_length = NcVar(long_name='Length of original unit hydrograph',
                         units='timesteps')

subset_length = NcVar(long_name='Shortened length of the unit hydrograph',
                      units='timesteps')

unit_hydrograph_dt = NcVar(long_name='Unit hydrograph timestep',
                           units='seconds')

outlet_x_ind = NcVar(long_name='x grid coordinate of outlet grid cell',
                     units='unitless')

outlet_y_ind = NcVar(long_name='y grid coordinate of outlet grid cell',
                     units='unitless')

outlet_lon = NcVar(long_name='Longitude coordinate of outlet grid cell',
                   units='degrees_east')

outlet_lat = NcVar(long_name='Latitude coordinate of outlet grid cell',
                   units='degrees_north')

outlet_decomp_ind = NcVar(long_name='1d grid location of outlet grid cell',
                          units='unitless')

outlet_number = NcVar(long_name='outlet number',
                      units='unitless')

outlet_mask = NcVar(long_name='type of outlet point',
                    units='0-ocean, 1-land, 2-guage, 3-none')

outlet_name = NcVar(long_name='Outlet guage name',
                    units='unitless')

source_x_ind = NcVar(long_name='x grid coordinate of source grid cell',
                     units='unitless')

source_y_ind = NcVar(long_name='y grid coordinate of source grid cell',
                     units='unitless')

source_lon = NcVar(long_name='Longitude coordinate of source grid cell',
                   units='degrees_east')

source_lat = NcVar(long_name='Latitude coordinate of source grid cell',
                   units='degrees_north')

source_decomp_ind = NcVar(long_name='1d grid location of source grid cell',
                          units='unitless')
source_time_offset = NcVar(long_name='Number of leading timesteps ommited',
                           units='timesteps')

source2outlet_ind = NcVar(long_name='source to outlet index mapping',
                          units='unitless')

ring = NcVar(long_name='Convolution Ring',
                   units='kg m-2 s-1')

streamflow = NcVar(long_name='Streamflow at outlet grid cell',
                   units='kg m-2 s-1')

storage = NcVar(long_name='Mass storage in stream upstream of outlet grid cell',
                units='kg m-2 s-1')

# valid values http://cf-pcmdi.llnl.gov/documents/cf-conventions/1.6/cf-conventions.html#calendar
timemgr_rst_type = NcVar(long_name='calendar type',
                         units='unitless')
timemgr_rst_type.flag_values = '0, 1, 2, 3, 4, 5, 6'
timemgr_rst_type.flag_meanings = 'NONE, NO_LEAP_C, GREGORIAN, PROLEPTIC_GREGORIAN, ALL_LEAP, 360_DAY, JULIAN'

timemgr_rst_step_sec = NcVar(long_name='seconds component of timestep size',
                             units='sec')
timemgr_rst_step_sec.valid_range = [0, 86400]

timemgr_rst_start_ymd = NcVar(long_name='start date',
                              units='YYYYMMDD')

timemgr_rst_start_tod = NcVar(long_name='start time of day',
                              units='sec')
timemgr_rst_step_sec.valid_range = [0, 86400]

timemgr_rst_ref_ymd = NcVar(long_name='reference date',
                            units='YYYYMMDD')

timemgr_rst_ref_tod = NcVar(long_name='reference time of day',
                            units='sec')
timemgr_rst_ref_tod.valid_range = [0, 86400]


timemgr_rst_curr_ymd = NcVar(long_name='current date',
                            units='YYYYMMDD')

timemgr_rst_curr_tod = NcVar(long_name='current time of day',
                            units='sec')
timemgr_rst_ref_tod.valid_range = [0, 86400]
