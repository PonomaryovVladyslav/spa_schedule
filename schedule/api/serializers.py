from rest_framework import serializers

from schedule.models import Schedule, Procedure, Record
from schedule.utils import SlotsValidator


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class FreeTimeCalculator(serializers.Serializer):
    procedure = serializers.PrimaryKeyRelatedField(queryset=Procedure.objects.all())


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def validate(self, data):
        if data['start_time'].strftime('%H:%M') not in SlotsValidator(data['schedule'], data['procedure']).ranges:
            raise serializers.ValidationError("Date is booked")
        return data
