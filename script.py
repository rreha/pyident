import osl, pspos
import pspnet

osl.initGfx(osl.PF_8888, True)
osl.setQuitOnLoadFailure(True)

sfont = osl.SFont("sfont.png")
osl.setBkColor(osl.RGBA(255,255,255,0))


skip = False

while not osl.mustQuit():
    if not skip:
        osl.startDrawing()
        batspecs = pspos.battery()
        msbytes = pspos.freemsspace()
        msmb = msbytes / 1024 / 1024

        sfont.drawString(0, 0,  "pyident 0.1.0 by reha")
        sfont.drawString(0, 30,  "# CPU frequency: %i MHZ" % pspos.getclock())
        sfont.drawString(0, 45,  "# BUS frequency: %i MHZ" % pspos.getbus())
        sfont.drawString(0, 60,  "# Free MS space: %i MB" % msmb)
        sfont.drawString(0, 75,  "# Remaining batt.: %i" % batspecs[3])
        sfont.drawString(0, 90,  "# Battery temp.: %i C" % batspecs[5])
        sfont.drawString(0, 105,  "# Battery volt.: %i mS" % batspecs[6])
        sfont.drawString(0, 135,  "Press O to quit =)")

        osl.endDrawing()
    osl.endFrame()
    skip = osl.syncFrame()

    ctrl = osl.Controller()
    if ctrl.held_circle:
        osl.safeQuit()

osl.endGfx()