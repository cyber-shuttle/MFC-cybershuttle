
import json, math

N = 100

ps = 248758.567
gam = 1.4
rho = 1.0
c_l = math.sqrt(1.4 * ps / rho)
vel = 230.0

leng = 1.0
Ny = N*leng
Nx = Ny * 3
dx = leng / Nx

time_end = 2 * leng / vel
cfl = 0.8

dt = cfl * dx / c_l
Nt = int(time_end / dt)

eps = 1e-8

# Configuring case dictionary
print(
    json.dumps(
        {
            # Logistics
            "run_time_info": "T",
            # Computational Domain Parameters
            "x_domain%beg": -leng / 2.0,
            "x_domain%end": leng / 2 + 2 * leng,
            "y_domain%beg": -leng / 2.0,
            "y_domain%end": leng / 2.0,
            "m": int(Nx),
            "n": int(Ny),
            "p": 0,
            "dt": dt,
            "t_step_start": 0,
            "t_step_stop": Nt,
            "t_step_save": int(Nt / 100),
            # Simulation Algorithm Parameters
            "num_patches": 3,
            "model_eqns": 2,
            "alt_soundspeed": "F",
            "num_fluids": 2,
            "mpp_lim": "T",
            "mixture_err": "T",
            "time_stepper": 3,
            "weno_order": 5,
            "weno_eps": 1.0e-16,
            "weno_Re_flux": "F",
            "weno_avg": "F",
            "mapped_weno": "T",
            "null_weights": "F",
            "mp_weno": "F",
            "riemann_solver": 2,
            "wave_speeds": 1,
            "avg_state": 2,
            "bc_x%beg": -6,
            "bc_x%end": -6,
            "bc_y%beg": -6,
            "bc_y%end": -6,
            # Formatted Database Files Structure Parameters
            "format": 1,
            "precision": 2,
            "prim_vars_wrt": "T",
            "parallel_io": "T",
            # Patch 1: Background
            "patch_icpp(1)%geometry": 3,
            "patch_icpp(1)%x_centroid": 0.0,
            "patch_icpp(1)%y_centroid": 0.0,
            "patch_icpp(1)%length_x": 10 * leng,
            "patch_icpp(1)%length_y": leng,
            "patch_icpp(1)%vel(1)": vel,
            "patch_icpp(1)%vel(2)": 0.0e00,
            "patch_icpp(1)%pres": 101325.0,
            "patch_icpp(1)%alpha_rho(1)": (1 - eps)*1.29,
            "patch_icpp(1)%alpha_rho(2)": eps,
            "patch_icpp(1)%alpha(1)": 1 - eps,
            "patch_icpp(1)%alpha(2)": eps,
            # Patch 2: Shocked state
            "patch_icpp(2)%geometry": 3,
            "patch_icpp(2)%alter_patch(1)": "T",
            "patch_icpp(2)%x_centroid": -3 * leng / 8.0,
            "patch_icpp(2)%y_centroid": 0.0,
            "patch_icpp(2)%length_x": leng / 4.0,
            "patch_icpp(2)%length_y": leng,
            "patch_icpp(2)%vel(1)": 0.0e00,
            "patch_icpp(2)%vel(2)": 0.0e00,
            "patch_icpp(2)%pres": ps,
            "patch_icpp(2)%alpha_rho(1)": (1 - eps)*2.4,
            "patch_icpp(2)%alpha_rho(2)": eps,
            "patch_icpp(2)%alpha(1)": 1 - eps,
            "patch_icpp(2)%alpha(2)": eps,
            # Patch 3: Bubble
            "patch_icpp(3)%geometry": 2,
            "patch_icpp(3)%x_centroid": 0.0e00,
            "patch_icpp(3)%y_centroid": 0.0e00,
            "patch_icpp(3)%radius": leng / 5.0,
            "patch_icpp(3)%alter_patch(1)": "T",
            "patch_icpp(3)%vel(1)": 0.0,
            "patch_icpp(3)%vel(2)": 0.0e00,
            "patch_icpp(3)%pres": 101325.0,
            "patch_icpp(3)%alpha_rho(1)": eps,
            "patch_icpp(3)%alpha_rho(2)": (1 - eps)*0.167,
            "patch_icpp(3)%alpha(1)": eps,
            "patch_icpp(3)%alpha(2)": 1 - eps,
            # Fluids Physical Parameters
            "fluid_pp(1)%gamma": 1.0e00 / (1.4e00 - 1.0e00),
            "fluid_pp(1)%pi_inf": 0.0,
            "fluid_pp(2)%gamma": 1.0e00 / (1.6666e00 - 1.0e00),
            "fluid_pp(2)%pi_inf": 0.0e00,
        }
    )
)