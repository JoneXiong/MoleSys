from peewee import *

database = MySQLDatabase('zkeco_db', **{'passwd': 'root', 'user': 'root'})

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Acc_Antiback(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    eight_mode = IntegerField()
    five_mode = IntegerField()
    four_mode = IntegerField()
    nine_mode = IntegerField()
    one_mode = IntegerField()
    seven_mode = IntegerField()
    six_mode = IntegerField()
    status = IntegerField()
    three_mode = IntegerField()
    two_mode = IntegerField()

    class Meta:
        db_table = 'acc_antiback'

class Acc_Auxin(BaseModel):
    auxin_name = CharField(null=True)
    auxin_no = IntegerField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    status = IntegerField()

    class Meta:
        db_table = 'acc_auxin'

class Acc_Device(BaseModel):
    isonlyrfmachine = IntegerField(null=True, db_column='IsOnlyRFMachine')
    aux_in_count = IntegerField(null=True)
    aux_out_count = IntegerField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    door_count = IntegerField(null=True)
    global_apb_on = IntegerField()
    iclock_server_on = IntegerField()
    machine_type = IntegerField(null=True)
    reader_count = IntegerField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'acc_device'

class Acc_Door(BaseModel):
    back_lock = IntegerField()
    card_intervaltime = IntegerField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    door_name = CharField(null=True)
    door_no = IntegerField(null=True)
    door_sensor_status = IntegerField(null=True)
    duration_apb = IntegerField(null=True)
    force_pwd = CharField(null=True)
    global_apb = IntegerField()
    inout_state = IntegerField(null=True)
    is_att = IntegerField()
    lock_active = IntegerField(null=True, db_column='lock_active_id')
    lock_delay = IntegerField(null=True)
    long_open = IntegerField(null=True, db_column='long_open_id')
    map = IntegerField(null=True, db_column='map_id')
    opendoor_type = IntegerField(null=True)
    reader_type = IntegerField(null=True)
    sensor_delay = IntegerField(null=True)
    status = IntegerField()
    supper_pwd = CharField(null=True)
    wiegand_fmt = IntegerField(null=True, db_column='wiegand_fmt_id')

    class Meta:
        db_table = 'acc_door'

class Acc_Firstopen(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    door = IntegerField(null=True, db_column='door_id')
    status = IntegerField()
    timeseg = IntegerField(null=True, db_column='timeseg_id')

    class Meta:
        db_table = 'acc_firstopen'

class Acc_Firstopen_Emp(BaseModel):
    accfirstopen = IntegerField(db_column='accfirstopen_id')
    employee = IntegerField(db_column='employee_id')

    class Meta:
        db_table = 'acc_firstopen_emp'

class Acc_Holidays(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    end_date = DateField()
    holiday_name = CharField(null=True)
    holiday_type = IntegerField(null=True)
    loop_by_year = IntegerField(null=True)
    memo = CharField(null=True)
    start_date = DateField()
    status = IntegerField()

    class Meta:
        db_table = 'acc_holidays'

class Acc_Interlock(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    four_mode = IntegerField()
    one_mode = IntegerField()
    status = IntegerField()
    three_mode = IntegerField()
    two_mode = IntegerField()

    class Meta:
        db_table = 'acc_interlock'

class Acc_Levelset(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    level_name = CharField(null=True)
    level_timeseg = IntegerField(null=True, db_column='level_timeseg_id')
    levelset_type = IntegerField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'acc_levelset'

class Acc_Levelset_Door_Group(BaseModel):
    accdoor = IntegerField(db_column='accdoor_id')
    acclevelset = IntegerField(db_column='acclevelset_id')

    class Meta:
        db_table = 'acc_levelset_door_group'

class Acc_Levelset_Emp(BaseModel):
    acclevelset = IntegerField(db_column='acclevelset_id')
    employee = IntegerField(db_column='employee_id')

    class Meta:
        db_table = 'acc_levelset_emp'

class Acc_Linkageio(BaseModel):
    action_type = IntegerField(null=True)
    alarm_voice_file = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delay_time = IntegerField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    in_address = IntegerField(null=True)
    in_address_hide = IntegerField(null=True)
    lchannel_num = IntegerField(null=True)
    linkage_name = CharField()
    linkage_type = IntegerField()
    out_address = IntegerField(null=True)
    out_address_hide = IntegerField(null=True)
    out_type_hide = IntegerField(null=True)
    status = IntegerField()
    trigger_opt = IntegerField(null=True)
    trigger_opt_fire = IntegerField(null=True)
    video_link_mode = IntegerField(null=True)
    video_linkageio = IntegerField(null=True, db_column='video_linkageio_id')

    class Meta:
        db_table = 'acc_linkageio'

class Acc_Linkageio_Auxin_Address_Fire(BaseModel):
    accauxin = IntegerField(db_column='accauxin_id')
    acclinkageio = IntegerField(db_column='acclinkageio_id')

    class Meta:
        db_table = 'acc_linkageio_auxin_address_fire'

class Acc_Linkageio_Door_Address_Fire(BaseModel):
    accdoor = IntegerField(db_column='accdoor_id')
    acclinkageio = IntegerField(db_column='acclinkageio_id')

    class Meta:
        db_table = 'acc_linkageio_door_address_fire'

class Acc_Map(BaseModel):
    area = IntegerField(null=True, db_column='area_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    height = FloatField(null=True)
    map_name = CharField(null=True)
    map_path = CharField(null=True)
    status = IntegerField()
    width = FloatField(null=True)

    class Meta:
        db_table = 'acc_map'

class Acc_Mapdoorpos(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    left = FloatField(null=True)
    map_door = IntegerField(null=True, db_column='map_door_id')
    map = IntegerField(null=True, db_column='map_id')
    status = IntegerField()
    top = FloatField(null=True)
    width = FloatField(null=True)

    class Meta:
        db_table = 'acc_mapdoorpos'

class Acc_Monitor_Log(BaseModel):
    card_no = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device = IntegerField(null=True, db_column='device_id')
    device_name = CharField(null=True)
    device_sn = CharField()
    door = IntegerField(null=True, db_column='door_id')
    door_name = CharField(null=True)
    event_type = IntegerField(null=True)
    in_address = IntegerField(null=True)
    log_tag = IntegerField(null=True)
    out_address = IntegerField(null=True)
    pin = CharField(null=True)
    state = IntegerField(null=True)
    status = IntegerField()
    time = DateTimeField(null=True)
    trigger_opt = IntegerField(null=True)
    verified = IntegerField(null=True)

    class Meta:
        db_table = 'acc_monitor_log'

class Acc_Morecardempgroup(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    group_name = CharField()
    memo = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'acc_morecardempgroup'

class Acc_Morecardgroup(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    comb = IntegerField(null=True, db_column='comb_id')
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    group = IntegerField(null=True, db_column='group_id')
    opener_number = IntegerField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'acc_morecardgroup'

class Acc_Morecardset(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    comb_name = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    door = IntegerField(null=True, db_column='door_id')
    status = IntegerField()

    class Meta:
        db_table = 'acc_morecardset'

class Acc_Timeseg(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    friday_end1 = TimeField()
    friday_end2 = TimeField()
    friday_end3 = TimeField()
    friday_start1 = TimeField()
    friday_start2 = TimeField()
    friday_start3 = TimeField()
    holidaytype1_end1 = TimeField()
    holidaytype1_end2 = TimeField()
    holidaytype1_end3 = TimeField()
    holidaytype1_start1 = TimeField()
    holidaytype1_start2 = TimeField()
    holidaytype1_start3 = TimeField()
    holidaytype2_end1 = TimeField()
    holidaytype2_end2 = TimeField()
    holidaytype2_end3 = TimeField()
    holidaytype2_start1 = TimeField()
    holidaytype2_start2 = TimeField()
    holidaytype2_start3 = TimeField()
    holidaytype3_end1 = TimeField()
    holidaytype3_end2 = TimeField()
    holidaytype3_end3 = TimeField()
    holidaytype3_start1 = TimeField()
    holidaytype3_start2 = TimeField()
    holidaytype3_start3 = TimeField()
    memo = CharField(null=True)
    monday_end1 = TimeField()
    monday_end2 = TimeField()
    monday_end3 = TimeField()
    monday_start1 = TimeField()
    monday_start2 = TimeField()
    monday_start3 = TimeField()
    saturday_end1 = TimeField()
    saturday_end2 = TimeField()
    saturday_end3 = TimeField()
    saturday_start1 = TimeField()
    saturday_start2 = TimeField()
    saturday_start3 = TimeField()
    status = IntegerField()
    sunday_end1 = TimeField()
    sunday_end2 = TimeField()
    sunday_end3 = TimeField()
    sunday_start1 = TimeField()
    sunday_start2 = TimeField()
    sunday_start3 = TimeField()
    thursday_end1 = TimeField()
    thursday_end2 = TimeField()
    thursday_end3 = TimeField()
    thursday_start1 = TimeField()
    thursday_start2 = TimeField()
    thursday_start3 = TimeField()
    timeseg_name = CharField()
    timeseg_type = IntegerField()
    tuesday_end1 = TimeField()
    tuesday_end2 = TimeField()
    tuesday_end3 = TimeField()
    tuesday_start1 = TimeField()
    tuesday_start2 = TimeField()
    tuesday_start3 = TimeField()
    wednesday_end1 = TimeField()
    wednesday_end2 = TimeField()
    wednesday_end3 = TimeField()
    wednesday_start1 = TimeField()
    wednesday_start2 = TimeField()
    wednesday_start3 = TimeField()

    class Meta:
        db_table = 'acc_timeseg'

class Acc_Wiegandfmt(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    cid_count = IntegerField(null=True)
    cid_start = IntegerField(null=True)
    comp_count = IntegerField(null=True)
    comp_start = IntegerField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    even_count = IntegerField(null=True)
    even_start = IntegerField(null=True)
    odd_count = IntegerField(null=True)
    odd_start = IntegerField(null=True)
    status = IntegerField()
    wiegand_count = IntegerField(null=True)
    wiegand_name = CharField()

    class Meta:
        db_table = 'acc_wiegandfmt'

class Action_Log(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = CharField()
    content_type = IntegerField(null=True, db_column='content_type_id')
    object = CharField(null=True, db_column='object_id')
    object_repr = CharField()
    user = IntegerField(null=True, db_column='user_id')

    class Meta:
        db_table = 'action_log'

class Areaadmin(BaseModel):
    area = IntegerField(db_column='area_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'areaadmin'

class Att_Attreport(BaseModel):
    author = IntegerField(db_column='Author_id')
    itemname = IntegerField(db_column='ItemName')
    itemtype = CharField(null=True, db_column='ItemType')
    itemvalue = TextField(null=True, db_column='ItemValue')
    published = IntegerField(null=True, db_column='Published')

    class Meta:
        db_table = 'att_attreport'

class Att_Overtime(BaseModel):
    audit_status = IntegerField()
    auditreason = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    emp = IntegerField(db_column='emp_id')
    endtime = DateTimeField()
    remark = CharField(null=True)
    starttime = DateTimeField()
    status = IntegerField()

    class Meta:
        db_table = 'att_overtime'

class Att_Waitforprocessdata(BaseModel):
    userid = IntegerField(db_column='UserID_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = DateTimeField()
    flag = IntegerField()
    starttime = DateTimeField()
    status = IntegerField()

    class Meta:
        db_table = 'att_waitforprocessdata'

class Attcalclog(BaseModel):
    deptid = IntegerField(null=True, db_column='DeptID')
    enddate = DateTimeField(db_column='EndDate')
    opertime = DateTimeField(db_column='OperTime')
    startdate = DateTimeField(null=True, db_column='StartDate')
    type = IntegerField(null=True, db_column='Type')
    userid = IntegerField(db_column='UserId')

    class Meta:
        db_table = 'attcalclog'

class Attexception(BaseModel):
    attdate = DateTimeField(null=True, db_column='AttDate')
    auditexcid = IntegerField(null=True, db_column='AuditExcID')
    endtime = DateTimeField(db_column='EndTime')
    exceptionid = IntegerField(null=True, db_column='ExceptionID')
    inscopetime = IntegerField(null=True, db_column='InScopeTime')
    minsworkday = IntegerField(null=True, db_column='Minsworkday')
    minsworkday1 = IntegerField(null=True, db_column='Minsworkday1')
    oldauditexcid = IntegerField(null=True, db_column='OldAuditExcID')
    overlaptime = IntegerField(null=True, db_column='OverlapTime')
    overlapworkday = FloatField(null=True, db_column='OverlapWorkDay')
    overlapworkdaytail = IntegerField(db_column='OverlapWorkDayTail')
    starttime = DateTimeField(db_column='StartTime')
    timelong = IntegerField(null=True, db_column='TimeLong')
    userid = IntegerField(db_column='UserId')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    schid = IntegerField(null=True)
    schindex = IntegerField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'attexception'

class Attparam(BaseModel):
    paraname = IntegerField(db_column='ParaName')
    paratype = CharField(null=True, db_column='ParaType')
    paravalue = CharField(db_column='ParaValue')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'attparam'

class Attrecabnormite(BaseModel):
    abnormiteid = IntegerField(null=True, db_column='AbNormiteID')
    attdate = DateTimeField(null=True, db_column='AttDate')
    checktype = CharField(db_column='CheckType')
    newtype = CharField(null=True, db_column='NewType')
    op = IntegerField(null=True, db_column='OP')
    schid = IntegerField(null=True, db_column='SchID')
    checktime = DateTimeField()
    userid = IntegerField()

    class Meta:
        db_table = 'attrecabnormite'

class Attshifts(BaseModel):
    absent = FloatField(null=True, db_column='Absent')
    absentmins = IntegerField(null=True, db_column='AbsentMins')
    absentr = FloatField(null=True, db_column='AbsentR')
    attchktime = CharField(null=True, db_column='AttChkTime')
    attdate = DateTimeField(db_column='AttDate')
    atttime = IntegerField(null=True, db_column='AttTime')
    autosch = IntegerField(null=True, db_column='AutoSch')
    clockintime = DateTimeField(db_column='ClockInTime')
    clockouttime = DateTimeField(db_column='ClockOutTime')
    early = FloatField(null=True, db_column='Early')
    endtime = DateTimeField(null=True, db_column='EndTime')
    exception = CharField(null=True, db_column='Exception')
    exceptionid = IntegerField(null=True, db_column='ExceptionID')
    isconfirm = IntegerField(null=True, db_column='IsConfirm')
    isread = IntegerField(null=True, db_column='IsRead')
    late = FloatField(null=True, db_column='Late')
    mustin = IntegerField(null=True, db_column='MustIn')
    mustout = IntegerField(null=True, db_column='MustOut')
    noin = IntegerField(null=True, db_column='NoIn')
    noout = IntegerField(null=True, db_column='NoOut')
    overtime = FloatField(null=True, db_column='OverTime')
    overtime1 = IntegerField(null=True, db_column='OverTime1')
    realworkday = FloatField(null=True, db_column='RealWorkDay')
    sspedayholiday = FloatField(null=True, db_column='SSpeDayHoliday')
    sspedayholidayot = FloatField(null=True, db_column='SSpeDayHolidayOT')
    sspedaynormal = FloatField(null=True, db_column='SSpeDayNormal')
    sspedaynormalot = FloatField(null=True, db_column='SSpeDayNormalOT')
    sspedayweekend = FloatField(null=True, db_column='SSpeDayWeekend')
    sspedayweekendot = FloatField(null=True, db_column='SSpeDayWeekendOT')
    schid = IntegerField(null=True, db_column='SchId')
    schindex = IntegerField(null=True, db_column='SchIndex')
    schedulename = CharField(null=True, db_column='ScheduleName')
    starttime = DateTimeField(null=True, db_column='StartTime')
    symbol = CharField(null=True, db_column='Symbol')
    workday = FloatField(null=True, db_column='WorkDay')
    workmins = IntegerField(null=True, db_column='WorkMins')
    worktime = IntegerField(null=True, db_column='WorkTime')
    userid = IntegerField()

    class Meta:
        db_table = 'attshifts'

class Auth_Group(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'auth_group'

class Auth_Group_Permissions(BaseModel):
    group = IntegerField(db_column='group_id')
    permission = IntegerField(db_column='permission_id')

    class Meta:
        db_table = 'auth_group_permissions'

class Auth_Message(BaseModel):
    message = TextField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'auth_message'

class Auth_Permission(BaseModel):
    codename = CharField()
    content_type = IntegerField(db_column='content_type_id')
    name = CharField()

    class Meta:
        db_table = 'auth_permission'

class Auth_User(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField()
    last_name = CharField()
    password = CharField()
    username = CharField()

    class Meta:
        db_table = 'auth_user'

class Auth_User_Groups(BaseModel):
    group = IntegerField(db_column='group_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'auth_user_groups'

class Auth_User_User_Permissions(BaseModel):
    permission = IntegerField(db_column='permission_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'auth_user_user_permissions'

class Base_Additiondata(BaseModel):
    content_type = IntegerField(null=True, db_column='content_type_id')
    create_time = DateTimeField()
    data = TextField()
    delete_time = DateTimeField(null=True)
    key = CharField()
    object = CharField(db_column='object_id')
    user = IntegerField(null=True, db_column='user_id')
    value = CharField()

    class Meta:
        db_table = 'base_additiondata'

class Base_Appoption(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    discribe = CharField(null=True)
    optname = CharField()
    status = IntegerField()
    value = CharField()

    class Meta:
        db_table = 'base_appoption'

class Base_Basecode(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    content = CharField()
    content_class = IntegerField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    display = CharField(null=True)
    is_add = CharField(null=True)
    remark = CharField(null=True)
    status = IntegerField()
    value = CharField()

    class Meta:
        db_table = 'base_basecode'

class Base_Datatranslation(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    content_type = IntegerField(null=True, db_column='content_type_id')
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    display = CharField()
    language = CharField()
    property = CharField()
    status = IntegerField()
    value = CharField()

    class Meta:
        db_table = 'base_datatranslation'

class Base_Operatortemplate(BaseModel):
    bio_type = IntegerField()
    bitmap_picture = TextField(null=True)
    bitmap_picture2 = TextField(null=True)
    bitmap_picture3 = TextField(null=True)
    bitmap_picture4 = TextField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    finger = IntegerField(db_column='finger_id')
    fpversion = CharField()
    status = IntegerField()
    template1 = TextField(null=True)
    template2 = TextField(null=True)
    template3 = TextField(null=True)
    template_flag = IntegerField()
    use_type = IntegerField(null=True)
    user = IntegerField(db_column='user_id')
    utime = DateTimeField(null=True)
    valid = IntegerField()

    class Meta:
        db_table = 'base_operatortemplate'

class Base_Option(BaseModel):
    app_label = CharField()
    catalog = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    default = CharField()
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    for_personal = IntegerField()
    group = CharField()
    help_text = CharField()
    name = CharField()
    read_only = IntegerField()
    required = IntegerField()
    status = IntegerField()
    type = CharField()
    validator = CharField()
    verbose_name = CharField()
    visible = IntegerField()
    widget = CharField()

    class Meta:
        db_table = 'base_option'

class Base_Personaloption(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    option = IntegerField(db_column='option_id')
    status = IntegerField()
    user = IntegerField(db_column='user_id')
    value = CharField()

    class Meta:
        db_table = 'base_personaloption'

class Base_Strresource(BaseModel):
    app = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()
    str = CharField()

    class Meta:
        db_table = 'base_strresource'

class Base_Strtranslation(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    display = CharField()
    language = CharField()
    status = IntegerField()
    str = IntegerField(db_column='str_id')

    class Meta:
        db_table = 'base_strtranslation'

class Base_Systemoption(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    option = IntegerField(db_column='option_id')
    status = IntegerField()
    value = CharField()

    class Meta:
        db_table = 'base_systemoption'

class Checkexact(BaseModel):
    checktime = DateTimeField(db_column='CHECKTIME')
    checktype = CharField(db_column='CHECKTYPE')
    date = DateTimeField(null=True, db_column='DATE')
    incount = IntegerField(null=True, db_column='INCOUNT')
    isadd = IntegerField(null=True, db_column='ISADD')
    iscount = IntegerField(null=True, db_column='ISCOUNT')
    isdelete = IntegerField(null=True, db_column='ISDELETE')
    ismodify = IntegerField(null=True, db_column='ISMODIFY')
    modifyby = CharField(null=True, db_column='MODIFYBY')
    userid = IntegerField(db_column='UserID')
    yuyin = CharField(null=True, db_column='YUYIN')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'checkexact'

class Checkinout(BaseModel):
    reserved = CharField(null=True, db_column='Reserved')
    sn = IntegerField(null=True, db_column='SN')
    workcode = CharField(null=True, db_column='WorkCode')
    checktime = DateTimeField()
    checktype = CharField(null=True)
    sensorid = CharField(null=True)
    sn_name = CharField(null=True)
    userid = IntegerField()
    verifycode = IntegerField()

    class Meta:
        db_table = 'checkinout'
        
    def __unicode__(self):
        return '%s: %s' % (self.userid, self.checktime)

class Dbapp_Viewmodel(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    info = TextField()
    model = IntegerField(db_column='model_id')
    name = CharField()
    status = IntegerField()
    viewtype = CharField()

    class Meta:
        db_table = 'dbapp_viewmodel'

class Dbbackuplog(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    imflag = IntegerField()
    starttime = DateTimeField(null=True)
    status = IntegerField()
    successflag = CharField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'dbbackuplog'

class Departments(BaseModel):
    deptid = IntegerField(db_column='DeptID')
    deptname = CharField(null=True, db_column='DeptName')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    invalidate = DateField(null=True)
    status = IntegerField()
    supdeptid = IntegerField(null=True)
    type = CharField()

    class Meta:
        db_table = 'departments'

class Deptadmin(BaseModel):
    dept = IntegerField(db_column='dept_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'deptadmin'

class Devcmds(BaseModel):
    cmdcommittime = DateTimeField(db_column='CmdCommitTime')
    cmdcontent = TextField(db_column='CmdContent')
    cmdimmediately = IntegerField(db_column='CmdImmediately')
    cmdoperate = IntegerField(null=True, db_column='CmdOperate_id')
    cmdovertime = DateTimeField(null=True, db_column='CmdOverTime')
    cmdreturn = IntegerField(null=True, db_column='CmdReturn')
    cmdreturncontent = TextField(null=True, db_column='CmdReturnContent')
    cmdtranstime = DateTimeField(null=True, db_column='CmdTransTime')
    sn = IntegerField(null=True, db_column='SN_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'devcmds'

class Devcmds_Bak(BaseModel):
    cmdcommittime = DateTimeField(db_column='CmdCommitTime')
    cmdcontent = TextField(db_column='CmdContent')
    cmdimmediately = IntegerField(db_column='CmdImmediately')
    cmdoperate = IntegerField(null=True, db_column='CmdOperate_id')
    cmdovertime = DateTimeField(null=True, db_column='CmdOverTime')
    cmdreturn = IntegerField(null=True, db_column='CmdReturn')
    cmdreturncontent = TextField(null=True, db_column='CmdReturnContent')
    cmdtranstime = DateTimeField(null=True, db_column='CmdTransTime')
    sn = IntegerField(null=True, db_column='SN_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'devcmds_bak'

class Devlog(BaseModel):
    cnt = IntegerField(db_column='Cnt')
    ecnt = IntegerField(db_column='ECnt')
    op = CharField(db_column='OP')
    object = CharField(null=True, db_column='Object')
    optime = DateTimeField(db_column='OpTime')
    sn = IntegerField(db_column='SN_id')

    class Meta:
        db_table = 'devlog'

class Django_Content_Type(BaseModel):
    app_label = CharField()
    model = CharField()
    name = CharField()

    class Meta:
        db_table = 'django_content_type'

class Django_Session(BaseModel):
    expire_date = DateTimeField()
    session_data = TextField()
    session_key = IntegerField()

    class Meta:
        db_table = 'django_session'

class Empitemdefine(BaseModel):
    author = IntegerField(db_column='Author_id')
    itemname = IntegerField(db_column='ItemName')
    itemtype = CharField(null=True, db_column='ItemType')
    itemvalue = TextField(null=True, db_column='ItemValue')
    published = IntegerField(null=True, db_column='Published')

    class Meta:
        db_table = 'empitemdefine'

class Holidays(BaseModel):
    duration = IntegerField(db_column='Duration')
    holidayday = IntegerField(null=True, db_column='HolidayDay')
    holidayid = IntegerField(db_column='HolidayID')
    holidaymonth = IntegerField(null=True, db_column='HolidayMonth')
    holidayname = CharField(db_column='HolidayName')
    holidaytype = IntegerField(null=True, db_column='HolidayType')
    holidayyear = IntegerField(null=True, db_column='HolidayYear')
    iscycle = IntegerField(db_column='IsCycle')
    minzu = CharField(null=True, db_column='MINZU')
    starttime = DateField(db_column='StartTime')
    xinbie = CharField(null=True, db_column='XINBIE')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'holidays'

class Iclock(BaseModel):
    accfun = IntegerField(db_column='AccFun')
    fpversion = CharField(null=True, db_column='Fpversion')
    tzadj = IntegerField(null=True, db_column='TZAdj')
    transinterval = IntegerField(null=True, db_column='TransInterval')
    updatedb = CharField(null=True, db_column='UpdateDB')
    acpanel_type = IntegerField(null=True)
    agent_ipaddress = CharField(null=True)
    alg_ver = CharField(null=True)
    alias = CharField()
    area = IntegerField(null=True, db_column='area_id')
    baudrate = IntegerField(null=True)
    brightness = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    city = CharField(null=True)
    com_address = IntegerField(null=True)
    com_port = IntegerField(null=True)
    comm_pwd = CharField(null=True)
    comm_type = IntegerField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delay = IntegerField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    device_name = CharField(null=True)
    device_type = IntegerField()
    dstime = IntegerField(null=True, db_column='dstime_id')
    dt_fmt = CharField(null=True)
    enabled = IntegerField()
    encrypt = IntegerField()
    flash_size = CharField(null=True)
    four_to_two = IntegerField()
    fp_count = IntegerField(null=True)
    fp_mthreshold = IntegerField(null=True)
    free_flash_size = CharField(null=True)
    fw_version = CharField(null=True)
    gateway = CharField(null=True)
    ip_port = IntegerField(null=True)
    ipaddress = CharField(null=True)
    is_tft = CharField(null=True)
    language = CharField(null=True)
    last_activity = DateTimeField(null=True)
    lng_encode = CharField(null=True)
    log_stamp = CharField(null=True)
    main_time = CharField(null=True)
    max_attlog_count = IntegerField(null=True)
    max_comm_count = IntegerField(null=True)
    max_comm_size = IntegerField(null=True)
    max_finger_count = IntegerField(null=True)
    max_user_count = IntegerField(null=True)
    oem_vendor = CharField(null=True)
    oplog_stamp = CharField(null=True)
    photo_stamp = CharField(null=True)
    platform = CharField(null=True)
    realtime = IntegerField()
    sn = CharField(null=True)
    status = IntegerField()
    subnet_mask = CharField(null=True)
    sync_time = IntegerField()
    trans_times = CharField(null=True)
    transaction_count = IntegerField(null=True)
    user_count = IntegerField(null=True)
    video_login = CharField(null=True)
    volume = CharField(null=True)

    class Meta:
        db_table = 'iclock'

class Iclock_Dstime(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    dst_name = CharField()
    end_time = CharField(null=True)
    mode = IntegerField(null=True)
    start_time = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'iclock_dstime'

class Iclock_Oplog(BaseModel):
    op = IntegerField(db_column='OP')
    optime = DateTimeField(db_column='OPTime')
    object = IntegerField(null=True, db_column='Object')
    param1 = IntegerField(null=True, db_column='Param1')
    param2 = IntegerField(null=True, db_column='Param2')
    param3 = IntegerField(null=True, db_column='Param3')
    sn = IntegerField(null=True, db_column='SN')
    admin = IntegerField()

    class Meta:
        db_table = 'iclock_oplog'

class Iclock_Testdata(BaseModel):
    area = IntegerField(null=True, db_column='area_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    dept = IntegerField(db_column='dept_id')
    status = IntegerField()

    class Meta:
        db_table = 'iclock_testdata'

class Iclock_Testdata_Admin_Area(BaseModel):
    area = IntegerField(db_column='area_id')
    testdata = IntegerField(db_column='testdata_id')

    class Meta:
        db_table = 'iclock_testdata_admin_area'

class Iclock_Testdata_Admin_Dept(BaseModel):
    department = IntegerField(db_column='department_id')
    testdata = IntegerField(db_column='testdata_id')

    class Meta:
        db_table = 'iclock_testdata_admin_dept'

class Johan_Music(BaseModel):
    author = CharField()
    path = TextField()
    title = CharField()
    type = CharField()

    class Meta:
        db_table = 'johan_music'

class Leaveclass(BaseModel):
    classify = IntegerField(db_column='Classify')
    color = IntegerField(db_column='Color')
    deduct = FloatField(null=True, db_column='Deduct')
    leaveid = IntegerField(db_column='LeaveID')
    leavename = CharField(db_column='LeaveName')
    leavetype = IntegerField(db_column='LeaveType')
    minunit = FloatField(db_column='MinUnit')
    remaindcount = IntegerField(db_column='RemaindCount')
    remaindproc = IntegerField(db_column='RemaindProc')
    reportsymbol = CharField(db_column='ReportSymbol')
    unit = IntegerField(db_column='Unit')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    clearance = IntegerField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'leaveclass'

class Leaveclass1(BaseModel):
    calc = TextField(null=True, db_column='Calc')
    classify = IntegerField(db_column='Classify')
    color = IntegerField(db_column='Color')
    deduct = FloatField(db_column='Deduct')
    leaveid = IntegerField(db_column='LeaveID')
    leavename = CharField(db_column='LeaveName')
    leavetype = IntegerField(db_column='LeaveType')
    minunit = FloatField(db_column='MinUnit')
    remaindcount = IntegerField(db_column='RemaindCount')
    remaindproc = IntegerField(db_column='RemaindProc')
    reportsymbol = CharField(db_column='ReportSymbol')
    unit = IntegerField(db_column='Unit')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'leaveclass1'

class Num_Run(BaseModel):
    cyle = IntegerField(db_column='Cyle')
    enddate = DateField(null=True, db_column='EndDate')
    name = CharField(db_column='Name')
    num_runid = IntegerField(db_column='Num_runID')
    oldid = IntegerField(null=True, db_column='OLDID')
    startdate = DateField(null=True, db_column='StartDate')
    units = IntegerField(db_column='Units')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'num_run'

class Num_Run_Deil(BaseModel):
    edays = IntegerField(null=True, db_column='Edays')
    endtime = TimeField(null=True, db_column='EndTime')
    num_runid = IntegerField(db_column='Num_runID')
    overtime = IntegerField(db_column='OverTime')
    schclassid = IntegerField(null=True, db_column='SchclassID')
    sdays = IntegerField(db_column='Sdays')
    starttime = TimeField(db_column='StartTime')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'num_run_deil'

class Operatecmds(BaseModel):
    author = IntegerField(null=True, db_column='Author_id')
    cmdcommittime = DateTimeField(db_column='CmdCommitTime')
    cmdcontent = TextField(db_column='CmdContent')
    cmdreturn = IntegerField(null=True, db_column='CmdReturn')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    cmm_system = IntegerField()
    cmm_type = IntegerField()
    commit_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    process_count = IntegerField()
    receive_data = TextField(null=True)
    status = IntegerField()
    success_flag = IntegerField()

    class Meta:
        db_table = 'operatecmds'

class Personnel_Area(BaseModel):
    areaid = CharField()
    areaname = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    parent = IntegerField(null=True, db_column='parent_id')
    remark = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'personnel_area'

class Personnel_Cardtype(BaseModel):
    cardtypecode = CharField()
    cardtypename = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'personnel_cardtype'

class Personnel_Cities(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = IntegerField(null=True)
    country = IntegerField(null=True, db_column='country_id')
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    state = IntegerField(null=True, db_column='state_id')
    status = IntegerField()

    class Meta:
        db_table = 'personnel_cities'

class Personnel_Countries(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'personnel_countries'

class Personnel_Education(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'personnel_education'

class Personnel_Empchange(BaseModel):
    userid = IntegerField(db_column='UserID_id')
    approvalstatus = IntegerField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    changedate = DateTimeField(null=True)
    changeno = IntegerField()
    changepostion = IntegerField(null=True)
    changereason = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    isvalid = IntegerField()
    newvalue = TextField(null=True)
    oldvalue = TextField(null=True)
    remark = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'personnel_empchange'

class Personnel_Issuecard(BaseModel):
    password = CharField(null=True, db_column='Password')
    userid = IntegerField(db_column='UserID_id')
    blance = DecimalField(null=True)
    card_cost = DecimalField(null=True)
    card_privage = CharField(null=True)
    card_serial_no = IntegerField(null=True)
    cardno = CharField()
    cardpwd = CharField(null=True)
    cardstatus = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    date_count = IntegerField(null=True)
    date_money = DecimalField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    effectivenessdate = DateField(null=True)
    failuredate = DateField(null=True)
    issuedate = DateField(null=True)
    isvalid = IntegerField()
    meal_count = IntegerField(null=True)
    meal_money = DecimalField(null=True)
    meal_type = IntegerField(null=True)
    mng_cost = DecimalField(null=True)
    pos_date = DateField(null=True)
    pos_time = DateTimeField(null=True)
    status = IntegerField()
    type = IntegerField(null=True, db_column='type_id')

    class Meta:
        db_table = 'personnel_issuecard'

class Personnel_Leavelog(BaseModel):
    userid = IntegerField(db_column='UserID_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    isclassaccess = IntegerField(db_column='isClassAccess')
    isclassatt = IntegerField(db_column='isClassAtt')
    isreturncard = IntegerField(db_column='isReturnCard')
    isreturnclothes = IntegerField(db_column='isReturnClothes')
    isreturntools = IntegerField(db_column='isReturnTools')
    leavedate = DateField()
    leavetype = IntegerField()
    reason = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'personnel_leavelog'

class Personnel_National(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'personnel_national'

class Personnel_Positions(BaseModel):
    deptid = IntegerField(null=True, db_column='DeptID_id')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'personnel_positions'

class Personnel_State(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = IntegerField(null=True)
    country = IntegerField(null=True, db_column='country_id')
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'personnel_state'

class Pos_Allowance(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    date = DateTimeField()
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    is_pass = IntegerField()
    money = DecimalField()
    pass_name = CharField(null=True)
    remark = CharField(null=True)
    status = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'pos_allowance'

class Pos_Allowancesetting(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    isadd = IntegerField()
    iszeor = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_allowancesetting'

class Pos_Batchtime(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = TimeField()
    isvalid = IntegerField()
    name = CharField(null=True)
    pos_time = CharField(null=True)
    remarks = CharField(null=True)
    starttime = TimeField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_batchtime'

class Pos_Carcashsz(BaseModel):
    blance = DecimalField(null=True)
    card = CharField()
    cardserial = IntegerField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    checktime = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    dining = CharField(null=True)
    discount = IntegerField(null=True)
    hide_column = IntegerField(null=True)
    money = DecimalField()
    serialnum = IntegerField(null=True)
    sn_name = CharField(null=True)
    status = IntegerField()
    type = IntegerField(db_column='type_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'pos_carcashsz'

class Pos_Carcashtype(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    remark = CharField(null=True)
    status = IntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'pos_carcashtype'

class Pos_Cardmanage(BaseModel):
    card_privage = CharField()
    cardno = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    passwd = CharField(null=True)
    status = IntegerField()
    time = DateTimeField(null=True)

    class Meta:
        db_table = 'pos_cardmanage'

class Pos_Dininghall(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = IntegerField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    remark = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_dininghall'

class Pos_Errors(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    errmemo = CharField(null=True)
    errmsg = CharField()
    errno = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_errors'

class Pos_Handconsume(BaseModel):
    blance = DecimalField(null=True)
    card_no = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    date = DateTimeField()
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    meal = IntegerField(db_column='meal_id')
    money = DecimalField()
    posdevice = IntegerField(db_column='posdevice_id')
    status = IntegerField()

    class Meta:
        db_table = 'pos_handconsume'

class Pos_Iccard(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    date_max_count = IntegerField()
    date_max_money = DecimalField()
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    discount = IntegerField()
    less_money = DecimalField()
    max_money = DecimalField()
    meal_max_count = IntegerField()
    meal_max_money = DecimalField()
    name = CharField()
    per_max_money = DecimalField()
    pos_time = CharField(null=True)
    remark = CharField()
    status = IntegerField()
    use_date = IntegerField()
    use_fingerprint = IntegerField()

    class Meta:
        db_table = 'pos_iccard'

class Pos_Iccard_Posmeal(BaseModel):
    iccard = IntegerField(db_column='iccard_id')
    meal = IntegerField(db_column='meal_id')

    class Meta:
        db_table = 'pos_iccard_posmeal'

class Pos_Iccard_Use_Mechine(BaseModel):
    device = IntegerField(db_column='device_id')
    iccard = IntegerField(db_column='iccard_id')

    class Meta:
        db_table = 'pos_iccard_use_mechine'

class Pos_Keyvalue(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = IntegerField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    money = DecimalField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_keyvalue'

class Pos_Keyvalue_Use_Mechine(BaseModel):
    device = IntegerField(db_column='device_id')
    keyvalue = IntegerField(db_column='keyvalue_id')

    class Meta:
        db_table = 'pos_keyvalue_use_mechine'

class Pos_Loseunitecard(BaseModel):
    cardno = CharField()
    cardstatus = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()
    time = DateTimeField(null=True)
    type = IntegerField(null=True, db_column='type_id')
    user = IntegerField(null=True, db_column='user_id')

    class Meta:
        db_table = 'pos_loseunitecard'

class Pos_Meal(BaseModel):
    available = IntegerField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = TimeField()
    money = DecimalField()
    name = CharField()
    remark = CharField()
    starttime = TimeField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_meal'

class Pos_Merchandise(BaseModel):
    barcode = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = IntegerField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    money = DecimalField()
    name = CharField()
    rebate = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_merchandise'

class Pos_Posdevlog(BaseModel):
    badgenumber = CharField(null=True)
    carno = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    content = CharField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    posoptime = DateTimeField(null=True, db_column='posOpTime')
    posmodel = IntegerField(null=True)
    remark = IntegerField(null=True)
    returncon = CharField(null=True)
    serialnum = CharField(null=True)
    sn = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'pos_posdevlog'

class Pos_Poslog(BaseModel):
    badgenumber = CharField(null=True)
    blance = DecimalField(null=True)
    carno = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    devname = CharField(null=True)
    posoptime = DateTimeField(null=True, db_column='posOpTime')
    posmodel = IntegerField(null=True)
    posmoney = DecimalField(null=True)
    serialnum = CharField(null=True)
    sn = CharField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'pos_poslog'

class Pos_Replenishcard(BaseModel):
    blance = DecimalField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    newcardno = CharField(null=True)
    oldcardno = CharField(null=True)
    status = IntegerField()
    time = DateTimeField(null=True)
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'pos_replenishcard'

class Pos_Splittime(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = TimeField()
    fixedmonery = DecimalField()
    isvalid = IntegerField()
    name = CharField()
    remarks = CharField(null=True)
    starttime = TimeField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_splittime'

class Pos_Splittime_Use_Mechine(BaseModel):
    device = IntegerField(db_column='device_id')
    splittime = IntegerField(db_column='splittime_id')

    class Meta:
        db_table = 'pos_splittime_use_mechine'

class Pos_Timebrush(BaseModel):
    begintime = DateTimeField(null=True)
    carno = CharField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = DateTimeField(null=True)
    serialnum = IntegerField(null=True)
    sn_name = CharField(null=True)
    status = IntegerField()
    type = IntegerField(null=True)

    class Meta:
        db_table = 'pos_timebrush'

class Pos_Timeslice(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    code = CharField()
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = TimeField()
    isvalid = IntegerField()
    remarks = CharField(null=True)
    starttime = TimeField()
    status = IntegerField()

    class Meta:
        db_table = 'pos_timeslice'

class Posparam(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    main_fan_area = CharField(null=True)
    max_money = DecimalField()
    minor_fan_area = CharField(null=True)
    pwd_again = CharField(null=True)
    status = IntegerField()
    system_pwd = CharField(null=True)

    class Meta:
        db_table = 'posparam'

class Report_Report(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    json_data = TextField(null=True)
    name = CharField()
    remark = CharField(null=True)
    report_type = IntegerField(null=True, db_column='report_type_id')
    status = IntegerField()
    user = IntegerField(null=True, db_column='user_id')

    class Meta:
        db_table = 'report_report'

class Report_Reporttype(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    name = CharField()
    remark = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'report_reporttype'

class Schclass(BaseModel):
    autobind = IntegerField(null=True, db_column='AutoBind')
    checkin = IntegerField(db_column='CheckIn')
    checkintime1 = TimeField(db_column='CheckInTime1')
    checkintime2 = TimeField(db_column='CheckInTime2')
    checkout = IntegerField(db_column='CheckOut')
    checkouttime1 = TimeField(db_column='CheckOutTime1')
    checkouttime2 = TimeField(db_column='CheckOutTime2')
    color = IntegerField(db_column='Color')
    earlyminutes = IntegerField(null=True, db_column='EarlyMinutes')
    endresttime = TimeField(null=True, db_column='EndRestTime')
    endresttime1 = TimeField(null=True, db_column='EndRestTime1')
    endtime = TimeField(db_column='EndTime')
    iscalcrest = IntegerField(null=True, db_column='IsCalcRest')
    isovertime = IntegerField(db_column='IsOverTime')
    lateminutes = IntegerField(null=True, db_column='LateMinutes')
    overtime = IntegerField(null=True, db_column='OverTime')
    schname = CharField(db_column='SchName')
    schclassid = IntegerField(db_column='SchclassID')
    startresttime = TimeField(null=True, db_column='StartRestTime')
    startresttime1 = TimeField(null=True, db_column='StartRestTime1')
    starttime = TimeField(db_column='StartTime')
    workday = FloatField(null=True, db_column='WorkDay')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    shiftworktime = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'schclass'

class Setuseratt(BaseModel):
    userid = IntegerField(null=True, db_column='UserID_id')
    atttype = IntegerField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    endtime = DateTimeField()
    starttime = DateTimeField()
    status = IntegerField()

    class Meta:
        db_table = 'setuseratt'

class Template(BaseModel):
    bitmappicture = TextField(null=True, db_column='BITMAPPICTURE')
    bitmappicture2 = TextField(null=True, db_column='BITMAPPICTURE2')
    bitmappicture3 = TextField(null=True, db_column='BITMAPPICTURE3')
    bitmappicture4 = TextField(null=True, db_column='BITMAPPICTURE4')
    fingerid = IntegerField(db_column='FingerID')
    fpversion = CharField(db_column='Fpversion')
    sn = IntegerField(null=True, db_column='SN')
    template = TextField(db_column='Template')
    template2 = TextField(null=True, db_column='Template2')
    template3 = TextField(null=True, db_column='Template3')
    usetype = IntegerField(null=True, db_column='USETYPE')
    utime = DateTimeField(null=True, db_column='UTime')
    valid = IntegerField(db_column='Valid')
    bio_type = IntegerField()
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()
    templateid = IntegerField()
    userid = IntegerField()

    class Meta:
        db_table = 'template'

class User_Of_Run(BaseModel):
    enddate = DateField(db_column='EndDate')
    isnotof_run = IntegerField(null=True, db_column='ISNOTOF_RUN')
    num_of_run = IntegerField(db_column='NUM_OF_RUN_ID')
    order_run = IntegerField(null=True, db_column='ORDER_RUN')
    startdate = DateField(db_column='StartDate')
    userid = IntegerField(db_column='UserID')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'user_of_run'

class User_Speday(BaseModel):
    date = DateTimeField(null=True, db_column='Date')
    dateid = IntegerField(db_column='DateID')
    endspecday = DateTimeField(null=True, db_column='EndSpecDay')
    startspecday = DateTimeField(db_column='StartSpecDay')
    state = CharField(null=True, db_column='State')
    userid = IntegerField(db_column='UserID')
    yuanying = CharField(null=True, db_column='YUANYING')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'user_speday'

class User_Temp_Sch(BaseModel):
    cometime = DateTimeField(db_column='ComeTime')
    flag = IntegerField(null=True, db_column='Flag')
    leavetime = DateTimeField(db_column='LeaveTime')
    overtime = IntegerField(db_column='OverTime')
    schclassid = IntegerField(null=True, db_column='SchClassID')
    type = IntegerField(null=True, db_column='Type')
    userid = IntegerField(db_column='UserID')
    worktype = IntegerField(db_column='WorkType')
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'user_temp_sch'

class Userinfo(BaseModel):
    att = IntegerField(db_column='ATT')
    accgroup = IntegerField(null=True, db_column='AccGroup')
    autoschplan = IntegerField(null=True, db_column='AutoSchPlan')
    birthday = DateField(null=True, db_column='Birthday')
    card = CharField(db_column='Card')
    city = CharField(null=True, db_column='City')
    cuser3 = CharField(null=True, db_column='Cuser3')
    cuser4 = CharField(null=True, db_column='Cuser4')
    cuser5 = CharField(null=True, db_column='Cuser5')
    deltag = IntegerField(db_column='DelTag')
    duser1 = DateField(null=True, db_column='Duser1')
    duser2 = DateField(null=True, db_column='Duser2')
    duser3 = DateField(null=True, db_column='Duser3')
    duser4 = DateField(null=True, db_column='Duser4')
    duser5 = DateField(null=True, db_column='Duser5')
    education = CharField(null=True, db_column='Education')
    fphone = CharField(null=True, db_column='FPHONE')
    gender = CharField(null=True, db_column='Gender')
    hiredday = DateField(null=True, db_column='Hiredday')
    holiday = IntegerField(db_column='Holiday')
    inlate = IntegerField(null=True, db_column='INLATE')
    iuser1 = IntegerField(null=True, db_column='Iuser1')
    iuser2 = IntegerField(null=True, db_column='Iuser2')
    iuser3 = IntegerField(null=True, db_column='Iuser3')
    iuser4 = IntegerField(null=True, db_column='Iuser4')
    iuser5 = IntegerField(null=True, db_column='Iuser5')
    lunchduration = IntegerField(null=True, db_column='Lunchduration')
    mverifypass = CharField(null=True, db_column='MVerifyPass')
    minautoschinterval = IntegerField(null=True, db_column='MinAutoSchInterval')
    offduty = IntegerField(db_column='OffDuty')
    outearly = IntegerField(null=True, db_column='OutEarly')
    overtime = IntegerField(db_column='OverTime')
    password = CharField(null=True, db_column='Password')
    political = CharField(null=True, db_column='Political')
    privilege = IntegerField(null=True, db_column='Privilege')
    registerot = IntegerField(null=True, db_column='RegisterOT')
    securityflags = IntegerField(null=True, db_column='SECURITYFLAGS')
    sep = IntegerField(null=True, db_column='SEP')
    ssn = CharField(null=True, db_column='SSN')
    state = CharField(null=True, db_column='State')
    timezones = CharField(null=True, db_column='TimeZones')
    utime = DateTimeField(null=True, db_column='UTime')
    verificationmethod = IntegerField(null=True, db_column='VERIFICATIONMETHOD')
    acc_enddate = DateField(null=True)
    acc_startdate = DateField(null=True)
    acc_super_auth = IntegerField(null=True)
    badgenumber = CharField()
    bankcode1 = CharField(null=True)
    bankcode2 = CharField(null=True)
    birthplace = CharField(null=True)
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    city = IntegerField(null=True, db_column='city_id')
    contry = CharField(null=True)
    country = IntegerField(null=True, db_column='country_id')
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    cuser1 = CharField(null=True)
    cuser2 = CharField(null=True)
    defaultdeptid = IntegerField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    education = IntegerField(null=True, db_column='education_id')
    email = CharField(null=True)
    emptype = IntegerField(null=True)
    firedate = DateField(null=True)
    fnumber = CharField(null=True)
    hiretype = IntegerField(null=True)
    homeaddress = CharField(null=True)
    identitycard = CharField(null=True)
    isatt = IntegerField()
    isblacklist = IntegerField(null=True)
    lastname = CharField(null=True)
    minzu = CharField(null=True)
    morecard_group = IntegerField(null=True, db_column='morecard_group_id')
    name = CharField(null=True)
    national = IntegerField(null=True, db_column='national_id')
    ophone = CharField(null=True)
    pager = CharField(null=True)
    photo = CharField()
    position = IntegerField(null=True, db_column='position_id')
    selfpassword = CharField(null=True)
    set_valid_time = IntegerField()
    state = IntegerField(null=True, db_column='state_id')
    status = IntegerField()
    street = CharField(null=True)
    title = CharField(null=True)
    userid = IntegerField()
    zip = CharField(null=True)

    class Meta:
        db_table = 'userinfo'

class Userinfo_Attarea(BaseModel):
    area = IntegerField(db_column='area_id')
    employee = IntegerField(db_column='employee_id')

    class Meta:
        db_table = 'userinfo_attarea'

class Useruusedsclasses(BaseModel):
    schid = IntegerField(null=True, db_column='SchId')
    userid = IntegerField(db_column='UserId')

    class Meta:
        db_table = 'useruusedsclasses'

class Worktable_Groupmsg(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    group = IntegerField(db_column='group_id')
    msgtype = IntegerField(db_column='msgtype_id')
    status = IntegerField()

    class Meta:
        db_table = 'worktable_groupmsg'


class Worktable_Msgtype(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    msg_ahead_remind = IntegerField()
    msg_keep_time = IntegerField()
    msgtype_name = CharField()
    msgtype_value = CharField()
    status = IntegerField()
    type = CharField()

    class Meta:
        db_table = 'worktable_msgtype'

class Worktable_Usrmsg(BaseModel):
    change_operator = CharField(null=True)
    change_time = DateTimeField(null=True)
    create_operator = CharField(null=True)
    create_time = DateTimeField(null=True)
    delete_operator = CharField(null=True)
    delete_time = DateTimeField(null=True)
    msg = IntegerField(null=True, db_column='msg_id')
    readtype = CharField(null=True)
    status = IntegerField()
    user = IntegerField(null=True, db_column='user_id')

    class Meta:
        db_table = 'worktable_usrmsg'

