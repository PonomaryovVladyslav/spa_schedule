from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from schedule.api.serializers import ScheduleSerializer, ProcedureSerializer, FreeTimeCalculator, RecordSerializer
from schedule.models import Schedule, Procedure, Record
from schedule.utils import SlotsValidator


class ScheduleModelViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @action(detail=True, methods=['GET'])
    def free(self, request, pk=None):
        schedule = self.get_object()
        serializer = FreeTimeCalculator(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        procedure = serializer.validated_data['procedure']
        return Response({'ranges': SlotsValidator(schedule, procedure).ranges})


class ProcedureModelViewSet(ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class RecordModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer