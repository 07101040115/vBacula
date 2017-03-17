# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import datetime
import json


BACULA_DB_EXIST = False

def model_is_managed():
    return not BACULA_DB_EXIST

class Basefiles(models.Model):
    baseid = models.AutoField(db_column='BaseId', primary_key=True)  # Field name made lowercase.
    basejobid = models.IntegerField(db_column='BaseJobId')  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    fileid = models.BigIntegerField(db_column='FileId')  # Field name made lowercase.
    fileindex = models.IntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'BaseFiles'


class Cdimages(models.Model):
    mediaid = models.IntegerField(db_column='MediaId', primary_key=True)  # Field name made lowercase.
    lastburn = models.DateTimeField(db_column='LastBurn')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'CDImages'


class Client(models.Model):
    clientid = models.AutoField(db_column='ClientId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.
    uname = models.TextField(db_column='Uname')  # Field name made lowercase.
    autoprune = models.IntegerField(db_column='AutoPrune', blank=True, null=True)  # Field name made lowercase.
    fileretention = models.BigIntegerField(db_column='FileRetention', blank=True, null=True)  # Field name made lowercase.
    jobretention = models.BigIntegerField(db_column='JobRetention', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class Counters(models.Model):
    counter = models.TextField(db_column='Counter', primary_key=True)  # Field name made lowercase.
    minvalue = models.IntegerField(db_column='MinValue', blank=True, null=True)  # Field name made lowercase.
    maxvalue = models.IntegerField(db_column='MaxValue', blank=True, null=True)  # Field name made lowercase.
    currentvalue = models.IntegerField(db_column='CurrentValue', blank=True, null=True)  # Field name made lowercase.
    wrapcounter = models.TextField(db_column='WrapCounter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counters'


class Device(models.Model):
    deviceid = models.AutoField(db_column='DeviceId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    mediatypeid = models.IntegerField(db_column='MediaTypeId', blank=True, null=True)  # Field name made lowercase.
    storageid = models.IntegerField(db_column='StorageId', blank=True, null=True)  # Field name made lowercase.
    devmounts = models.IntegerField(db_column='DevMounts', blank=True, null=True)  # Field name made lowercase.
    devreadbytes = models.BigIntegerField(db_column='DevReadBytes', blank=True, null=True)  # Field name made lowercase.
    devwritebytes = models.BigIntegerField(db_column='DevWriteBytes', blank=True, null=True)  # Field name made lowercase.
    devreadbytessincecleaning = models.BigIntegerField(db_column='DevReadBytesSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devwritebytessincecleaning = models.BigIntegerField(db_column='DevWriteBytesSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devreadtime = models.BigIntegerField(db_column='DevReadTime', blank=True, null=True)  # Field name made lowercase.
    devwritetime = models.BigIntegerField(db_column='DevWriteTime', blank=True, null=True)  # Field name made lowercase.
    devreadtimesincecleaning = models.BigIntegerField(db_column='DevReadTimeSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    devwritetimesincecleaning = models.BigIntegerField(db_column='DevWriteTimeSinceCleaning', blank=True, null=True)  # Field name made lowercase.
    cleaningdate = models.DateTimeField(db_column='CleaningDate', blank=True, null=True)  # Field name made lowercase.
    cleaningperiod = models.BigIntegerField(db_column='CleaningPeriod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device'


class File(models.Model):
    fileid = models.BigIntegerField(db_column='FileId', primary_key=True)  # Field name made lowercase.
    fileindex = models.IntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    pathid = models.IntegerField(db_column='PathId')  # Field name made lowercase.
    filenameid = models.IntegerField(db_column='FilenameId')  # Field name made lowercase.
    deltaseq = models.SmallIntegerField(db_column='DeltaSeq', blank=True, null=True)  # Field name made lowercase.
    markid = models.IntegerField(db_column='MarkId', blank=True, null=True)  # Field name made lowercase.
    lstat = models.TextField(db_column='LStat')  # Field name made lowercase.
    md5 = models.TextField(db_column='MD5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'File'


class Fileset(models.Model):
    filesetid = models.AutoField(db_column='FileSetId', primary_key=True)  # Field name made lowercase.
    fileset = models.TextField(db_column='FileSet')  # Field name made lowercase.
    md5 = models.TextField(db_column='MD5', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'FileSet'


class Filename(models.Model):
    filenameid = models.AutoField(db_column='FilenameId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Filename'


class Job(models.Model):
    jobid = models.AutoField(db_column='JobId', primary_key=True)  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=1)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    jobstatus = models.CharField(db_column='JobStatus', max_length=1)  # Field name made lowercase.
    schedtime = models.DateTimeField(db_column='SchedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='RealEndTime', blank=True, null=True)  # Field name made lowercase.
    jobtdate = models.BigIntegerField(db_column='JobTDate', blank=True, null=True)  # Field name made lowercase.
    volsessionid = models.IntegerField(db_column='VolSessionId', blank=True, null=True)  # Field name made lowercase.
    volsessiontime = models.IntegerField(db_column='VolSessionTime', blank=True, null=True)  # Field name made lowercase.
    jobfiles = models.IntegerField(db_column='JobFiles', blank=True, null=True)  # Field name made lowercase.
    jobbytes = models.BigIntegerField(db_column='JobBytes', blank=True, null=True)  # Field name made lowercase.
    readbytes = models.BigIntegerField(db_column='ReadBytes', blank=True, null=True)  # Field name made lowercase.
    joberrors = models.IntegerField(db_column='JobErrors', blank=True, null=True)  # Field name made lowercase.
    jobmissingfiles = models.IntegerField(db_column='JobMissingFiles', blank=True, null=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    filesetid = models.IntegerField(db_column='FileSetId', blank=True, null=True)  # Field name made lowercase.
    priorjobid = models.IntegerField(db_column='PriorJobId', blank=True, null=True)  # Field name made lowercase.
    purgedfiles = models.IntegerField(db_column='PurgedFiles', blank=True, null=True)  # Field name made lowercase.
    hasbase = models.IntegerField(db_column='HasBase', blank=True, null=True)  # Field name made lowercase.
    hascache = models.IntegerField(db_column='HasCache', blank=True, null=True)  # Field name made lowercase.
    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    filetable = models.CharField(db_column='FileTable', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Job'

    def __str__(self):
        return 'jobid = %s' % self.jobid
    
    def __unicode__(self):
        return 'jobid = %s' % self.jobid
     
     
    def as_json(self):
        print self.endtime - self.starttime
        return dict(jobid = self.jobid, name = self.name,
                    jobstatus = self.jobstatus, level = self.level,
                    jobfiles = self.jobfiles, jobbytes = self.jobbytes,
                    joberrors = self.joberrors, clientname = self.clientid,
                    starttime = self.starttime.strftime('%Y-%m-%d %H:%M:%S'),
                    endtime = self.endtime.strftime('%Y-%m-%d %H:%M:%S'),
                    durationtime = str(self.endtime - self.starttime)
                   )
        
class Jobhisto(models.Model):
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=1)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    jobstatus = models.CharField(db_column='JobStatus', max_length=1)  # Field name made lowercase.
    schedtime = models.DateTimeField(db_column='SchedTime', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    realendtime = models.DateTimeField(db_column='RealEndTime', blank=True, null=True)  # Field name made lowercase.
    jobtdate = models.BigIntegerField(db_column='JobTDate', blank=True, null=True)  # Field name made lowercase.
    volsessionid = models.IntegerField(db_column='VolSessionId', blank=True, null=True)  # Field name made lowercase.
    volsessiontime = models.IntegerField(db_column='VolSessionTime', blank=True, null=True)  # Field name made lowercase.
    jobfiles = models.IntegerField(db_column='JobFiles', blank=True, null=True)  # Field name made lowercase.
    jobbytes = models.BigIntegerField(db_column='JobBytes', blank=True, null=True)  # Field name made lowercase.
    readbytes = models.BigIntegerField(db_column='ReadBytes', blank=True, null=True)  # Field name made lowercase.
    joberrors = models.IntegerField(db_column='JobErrors', blank=True, null=True)  # Field name made lowercase.
    jobmissingfiles = models.IntegerField(db_column='JobMissingFiles', blank=True, null=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    filesetid = models.IntegerField(db_column='FileSetId', blank=True, null=True)  # Field name made lowercase.
    priorjobid = models.IntegerField(db_column='PriorJobId', blank=True, null=True)  # Field name made lowercase.
    purgedfiles = models.IntegerField(db_column='PurgedFiles', blank=True, null=True)  # Field name made lowercase.
    hasbase = models.IntegerField(db_column='HasBase', blank=True, null=True)  # Field name made lowercase.
    hascache = models.IntegerField(db_column='HasCache', blank=True, null=True)  # Field name made lowercase.
    reviewed = models.IntegerField(db_column='Reviewed', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    filetable = models.CharField(db_column='FileTable', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobHisto'


class Jobmedia(models.Model):
    jobmediaid = models.AutoField(db_column='JobMediaId', primary_key=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaId')  # Field name made lowercase.
    firstindex = models.IntegerField(db_column='FirstIndex', blank=True, null=True)  # Field name made lowercase.
    lastindex = models.IntegerField(db_column='LastIndex', blank=True, null=True)  # Field name made lowercase.
    startfile = models.IntegerField(db_column='StartFile', blank=True, null=True)  # Field name made lowercase.
    endfile = models.IntegerField(db_column='EndFile', blank=True, null=True)  # Field name made lowercase.
    startblock = models.IntegerField(db_column='StartBlock', blank=True, null=True)  # Field name made lowercase.
    endblock = models.IntegerField(db_column='EndBlock', blank=True, null=True)  # Field name made lowercase.
    volindex = models.IntegerField(db_column='VolIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'JobMedia'


class Location(models.Model):
    locationid = models.AutoField(db_column='LocationId', primary_key=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location')  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Location'


class Locationlog(models.Model):
    loclogid = models.AutoField(db_column='LocLogId', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaId', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    newvolstatus = models.CharField(db_column='NewVolStatus', max_length=9)  # Field name made lowercase.
    newenabled = models.IntegerField(db_column='NewEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'LocationLog'


class Log(models.Model):
    logid = models.AutoField(db_column='LogId', primary_key=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    logtext = models.TextField(db_column='LogText')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Log'


class Media(models.Model):
    mediaid = models.AutoField(db_column='MediaId', primary_key=True)  # Field name made lowercase.
    volumename = models.TextField(db_column='VolumeName', unique=True)  # Field name made lowercase.
    slot = models.IntegerField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolId', blank=True, null=True)  # Field name made lowercase.
    mediatype = models.TextField(db_column='MediaType')  # Field name made lowercase.
    mediatypeid = models.IntegerField(db_column='MediaTypeId', blank=True, null=True)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='LabelType', blank=True, null=True)  # Field name made lowercase.
    firstwritten = models.DateTimeField(db_column='FirstWritten', blank=True, null=True)  # Field name made lowercase.
    lastwritten = models.DateTimeField(db_column='LastWritten', blank=True, null=True)  # Field name made lowercase.
    labeldate = models.DateTimeField(db_column='LabelDate', blank=True, null=True)  # Field name made lowercase.
    voljobs = models.IntegerField(db_column='VolJobs', blank=True, null=True)  # Field name made lowercase.
    volfiles = models.IntegerField(db_column='VolFiles', blank=True, null=True)  # Field name made lowercase.
    volblocks = models.IntegerField(db_column='VolBlocks', blank=True, null=True)  # Field name made lowercase.
    volmounts = models.IntegerField(db_column='VolMounts', blank=True, null=True)  # Field name made lowercase.
    volbytes = models.BigIntegerField(db_column='VolBytes', blank=True, null=True)  # Field name made lowercase.
    volabytes = models.BigIntegerField(db_column='VolABytes', blank=True, null=True)  # Field name made lowercase.
    volapadding = models.BigIntegerField(db_column='VolAPadding', blank=True, null=True)  # Field name made lowercase.
    volholebytes = models.BigIntegerField(db_column='VolHoleBytes', blank=True, null=True)  # Field name made lowercase.
    volholes = models.IntegerField(db_column='VolHoles', blank=True, null=True)  # Field name made lowercase.
    volparts = models.IntegerField(db_column='VolParts', blank=True, null=True)  # Field name made lowercase.
    volerrors = models.IntegerField(db_column='VolErrors', blank=True, null=True)  # Field name made lowercase.
    volwrites = models.BigIntegerField(db_column='VolWrites', blank=True, null=True)  # Field name made lowercase.
    volcapacitybytes = models.BigIntegerField(db_column='VolCapacityBytes', blank=True, null=True)  # Field name made lowercase.
    volstatus = models.CharField(db_column='VolStatus', max_length=9)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    recycle = models.IntegerField(db_column='Recycle', blank=True, null=True)  # Field name made lowercase.
    actiononpurge = models.IntegerField(db_column='ActionOnPurge', blank=True, null=True)  # Field name made lowercase.
    volretention = models.BigIntegerField(db_column='VolRetention', blank=True, null=True)  # Field name made lowercase.
    voluseduration = models.BigIntegerField(db_column='VolUseDuration', blank=True, null=True)  # Field name made lowercase.
    maxvoljobs = models.IntegerField(db_column='MaxVolJobs', blank=True, null=True)  # Field name made lowercase.
    maxvolfiles = models.IntegerField(db_column='MaxVolFiles', blank=True, null=True)  # Field name made lowercase.
    maxvolbytes = models.BigIntegerField(db_column='MaxVolBytes', blank=True, null=True)  # Field name made lowercase.
    inchanger = models.IntegerField(db_column='InChanger', blank=True, null=True)  # Field name made lowercase.
    storageid = models.IntegerField(db_column='StorageId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    mediaaddressing = models.IntegerField(db_column='MediaAddressing', blank=True, null=True)  # Field name made lowercase.
    volreadtime = models.BigIntegerField(db_column='VolReadTime', blank=True, null=True)  # Field name made lowercase.
    volwritetime = models.BigIntegerField(db_column='VolWriteTime', blank=True, null=True)  # Field name made lowercase.
    endfile = models.IntegerField(db_column='EndFile', blank=True, null=True)  # Field name made lowercase.
    endblock = models.IntegerField(db_column='EndBlock', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId', blank=True, null=True)  # Field name made lowercase.
    recyclecount = models.IntegerField(db_column='RecycleCount', blank=True, null=True)  # Field name made lowercase.
    initialwrite = models.DateTimeField(db_column='InitialWrite', blank=True, null=True)  # Field name made lowercase.
    scratchpoolid = models.IntegerField(db_column='ScratchPoolId', blank=True, null=True)  # Field name made lowercase.
    recyclepoolid = models.IntegerField(db_column='RecyclePoolId', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Media'


class Mediatype(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    mediatype = models.TextField(db_column='MediaType')  # Field name made lowercase.
    readonly = models.IntegerField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'MediaType'


class Path(models.Model):
    pathid = models.AutoField(db_column='PathId', primary_key=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Path'


class Pathhierarchy(models.Model):
    pathid = models.IntegerField(db_column='PathId', primary_key=True)  # Field name made lowercase.
    ppathid = models.IntegerField(db_column='PPathId')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'PathHierarchy'


class Pathvisibility(models.Model):
    pathid = models.IntegerField(db_column='PathId')  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    size = models.BigIntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    files = models.IntegerField(db_column='Files', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'PathVisibility'
        unique_together = (('jobid', 'pathid'),)


class Pool(models.Model):
    poolid = models.AutoField(db_column='PoolId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.
    numvols = models.IntegerField(db_column='NumVols', blank=True, null=True)  # Field name made lowercase.
    maxvols = models.IntegerField(db_column='MaxVols', blank=True, null=True)  # Field name made lowercase.
    useonce = models.IntegerField(db_column='UseOnce', blank=True, null=True)  # Field name made lowercase.
    usecatalog = models.IntegerField(db_column='UseCatalog', blank=True, null=True)  # Field name made lowercase.
    acceptanyvolume = models.IntegerField(db_column='AcceptAnyVolume', blank=True, null=True)  # Field name made lowercase.
    volretention = models.BigIntegerField(db_column='VolRetention', blank=True, null=True)  # Field name made lowercase.
    voluseduration = models.BigIntegerField(db_column='VolUseDuration', blank=True, null=True)  # Field name made lowercase.
    maxvoljobs = models.IntegerField(db_column='MaxVolJobs', blank=True, null=True)  # Field name made lowercase.
    maxvolfiles = models.IntegerField(db_column='MaxVolFiles', blank=True, null=True)  # Field name made lowercase.
    maxvolbytes = models.BigIntegerField(db_column='MaxVolBytes', blank=True, null=True)  # Field name made lowercase.
    autoprune = models.IntegerField(db_column='AutoPrune', blank=True, null=True)  # Field name made lowercase.
    recycle = models.IntegerField(db_column='Recycle', blank=True, null=True)  # Field name made lowercase.
    actiononpurge = models.IntegerField(db_column='ActionOnPurge', blank=True, null=True)  # Field name made lowercase.
    pooltype = models.CharField(db_column='PoolType', max_length=9)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='LabelType', blank=True, null=True)  # Field name made lowercase.
    labelformat = models.TextField(db_column='LabelFormat', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    scratchpoolid = models.IntegerField(db_column='ScratchPoolId', blank=True, null=True)  # Field name made lowercase.
    recyclepoolid = models.IntegerField(db_column='RecyclePoolId', blank=True, null=True)  # Field name made lowercase.
    nextpoolid = models.IntegerField(db_column='NextPoolId', blank=True, null=True)  # Field name made lowercase.
    migrationhighbytes = models.BigIntegerField(db_column='MigrationHighBytes', blank=True, null=True)  # Field name made lowercase.
    migrationlowbytes = models.BigIntegerField(db_column='MigrationLowBytes', blank=True, null=True)  # Field name made lowercase.
    migrationtime = models.BigIntegerField(db_column='MigrationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pool'


class Restoreobject(models.Model):
    restoreobjectid = models.AutoField(db_column='RestoreObjectId', primary_key=True)  # Field name made lowercase.
    objectname = models.TextField(db_column='ObjectName')  # Field name made lowercase.
    restoreobject = models.TextField(db_column='RestoreObject')  # Field name made lowercase.
    pluginname = models.TextField(db_column='PluginName')  # Field name made lowercase.
    objectlength = models.IntegerField(db_column='ObjectLength', blank=True, null=True)  # Field name made lowercase.
    objectfulllength = models.IntegerField(db_column='ObjectFullLength', blank=True, null=True)  # Field name made lowercase.
    objectindex = models.IntegerField(db_column='ObjectIndex', blank=True, null=True)  # Field name made lowercase.
    objecttype = models.IntegerField(db_column='ObjectType', blank=True, null=True)  # Field name made lowercase.
    fileindex = models.IntegerField(db_column='FileIndex', blank=True, null=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    objectcompression = models.IntegerField(db_column='ObjectCompression', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'RestoreObject'


class Snapshot(models.Model):
    snapshotid = models.AutoField(db_column='SnapshotId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId', blank=True, null=True)  # Field name made lowercase.
    filesetid = models.IntegerField(db_column='FileSetId', blank=True, null=True)  # Field name made lowercase.
    createtdate = models.BigIntegerField(db_column='CreateTDate')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='Volume')  # Field name made lowercase.
    device = models.TextField(db_column='Device')  # Field name made lowercase.
    type = models.TextField(db_column='Type')  # Field name made lowercase.
    retention = models.IntegerField(db_column='Retention', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Snapshot'
        unique_together = (('device', 'volume', 'name'),)


class Status(models.Model):
    jobstatus = models.CharField(db_column='JobStatus', primary_key=True, max_length=1)  # Field name made lowercase.
    jobstatuslong = models.TextField(db_column='JobStatusLong', blank=True, null=True)  # Field name made lowercase.
    severity = models.IntegerField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Status'


class Storage(models.Model):
    storageid = models.AutoField(db_column='StorageId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    autochanger = models.IntegerField(db_column='AutoChanger', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Storage'


class Unsavedfiles(models.Model):
    unsavedid = models.AutoField(db_column='UnsavedId', primary_key=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='JobId')  # Field name made lowercase.
    pathid = models.IntegerField(db_column='PathId')  # Field name made lowercase.
    filenameid = models.IntegerField(db_column='FilenameId')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'UnsavedFiles'


class Version(models.Model):
    versionid = models.IntegerField(db_column='VersionId')  # Field name made lowercase.

    class Meta:
        managed = model_is_managed()
        db_table = 'Version'

class WebaculaClientAcl(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    order_acl = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_client_acl'
        unique_together = (('name', 'role_id'),)


class WebaculaCommandAcl(models.Model):
    dt_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_command_acl'
        unique_together = (('dt_id', 'role_id'),)


class WebaculaDtCommands(models.Model):
    name = models.CharField(unique=True, max_length=127)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = 'webacula_dt_commands'


class WebaculaDtResources(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = 'webacula_dt_resources'


class WebaculaFilesetAcl(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    order_acl = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_fileset_acl'
        unique_together = (('name', 'role_id'),)


class WebaculaJobAcl(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    order_acl = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_job_acl'
        unique_together = (('name', 'role_id'),)


class WebaculaJobdesc(models.Model):
    desc_id = models.AutoField(primary_key=True)
    name_job = models.CharField(unique=True, max_length=64)
    retention_period = models.CharField(max_length=32, blank=True, null=True)
    short_desc = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = 'webacula_jobdesc'


class WebaculaLogbook(models.Model):
    logid = models.AutoField(db_column='logId', primary_key=True)  # Field name made lowercase.
    logdatecreate = models.DateTimeField(db_column='logDateCreate')  # Field name made lowercase.
    logdatelast = models.DateTimeField(db_column='logDateLast', blank=True, null=True)  # Field name made lowercase.
    logtxt = models.TextField(db_column='logTxt')  # Field name made lowercase.
    logtypeid = models.IntegerField(db_column='logTypeId')  # Field name made lowercase.
    logisdel = models.IntegerField(db_column='logIsDel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'webacula_logbook'


class WebaculaLogtype(models.Model):
    typeid = models.IntegerField(db_column='typeId', primary_key=True)  # Field name made lowercase.
    typedesc = models.TextField(db_column='typeDesc')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'webacula_logtype'


class WebaculaPhpSession(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    modified = models.IntegerField(blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)
    data_session = models.TextField(blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_php_session'


class WebaculaPoolAcl(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    order_acl = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_pool_acl'
        unique_together = (('name', 'role_id'),)


class WebaculaResources(models.Model):
    dt_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_resources'


class WebaculaRoles(models.Model):
    order_role = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    inherit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_roles'


class WebaculaStorageAcl(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    order_acl = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webacula_storage_acl'
        unique_together = (('name', 'role_id'),)


class WebaculaUsers(models.Model):
    login = models.CharField(unique=True, max_length=50)
    pwd = models.CharField(max_length=256)
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    create_login = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=40, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'webacula_users'


class WebaculaVersion(models.Model):
    versionid = models.IntegerField(db_column='versionId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'webacula_version'

#error :  django.db.utils.OperationalError: (1170, "BLOB/TEXT column 'name' used in key specification without a key length")
# class WebaculaWhereAcl(models.Model):
#     name = models.TextField(max_length = 100)
#     order_acl = models.IntegerField(blank=True, null=True)
#     role_id = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = True
#         db_table = 'webacula_where_acl'
#         unique_together = (('name', 'role_id'),)
