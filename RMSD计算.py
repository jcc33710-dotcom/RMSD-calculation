from pymol import cmd
import pymol

# 启动 PyMOL（无 GUI）
pymol.finish_launching(['pymol', '-cq'])
# -c: command line only
# -q: quiet

cmd.delete("control")
cmd.delete("bait")
# 读入结构
cmd.load(r"C:\Users\Lenovo\Desktop\jyc毕业论文\实验数据\AF3\筛选ipTM\SCOOOP12_MIK2\scoop12_mik2_bak1\fold_scoop12_mik2_bak1_model_0.cif", "control")
cmd.load(r"C:\Users\Lenovo\Desktop\jyc毕业论文\实验数据\AF3\筛选ipTM\SCOOOP12_MIK2\scoop12_mik2_AT1G25320\fold_scoop12_mik2_lrr192_model_0.cif", "bait")
# 构建全局选择
global_sel_control = "name CA and control "
global_sel_bait = "name CA and bait "
# 对齐并返回 RMSD
global_rmsd = cmd.align(global_sel_control, global_sel_bait)[0]
print("Global RMSD:", global_rmsd)

