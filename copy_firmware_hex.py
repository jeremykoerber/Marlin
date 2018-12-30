Import("env")
env.AlwaysBuild(env.Alias("buildfw", None, ["cp .pioenvs/megaatmega2560/firmware.hex ~/3dprint"]))
