import matplotlib.pyplot as plt
import numpy as np
from sys import exit
from sys import argv

# return times in seconds
def process_time(s):
    # Strip last two letters (always 's\n')
    s = s[:-2]
    if s[-1].isdigit():
        # This is in seconds already
        return float(s)
    if s[-1] == 'm':
        # This is in millisecs
        return float(s[:-1]) / 1000
    # These are microsecs
    return float(s[:-1]) / 1000000

def from_file(path):
    f = open(path)
    v = []
    for l in f.readlines():
        x = process_time(l)
        v.append(x)
    return v



V_SZs = [16384 ,  32768 ,  65536 ,  131072 ,  262144 ,  524288 ,  1048576]
LOG_V_SZs = [i for i in range(14, 21)]
OPN_SZs = [256, 2048, 16384]


N_AMORTS = list(range(10,1000,20))
# Next values are for amortization
v_sz_idx = 4 # 128K bits
opn_idx = 1 # many bits opening

LBLs = ['pre_yy', 'yy', 'bbf']

def data_opn_files(s):
    return [f'opn_{s}_{o}' for o in OPN_SZs]

def data_vfy_files(s):
    return [f'vfy_{s}_{o}' for o in OPN_SZs]

def extend_to_amm(d, m):
    
    l = len(V_SZs)
    compute_amm = lambda c, o: c/m + o
    return compute_amm(d['com'][v_sz_idx], d['opn'][opn_idx][v_sz_idx]) 

def mk_record(lbl):
    basic_record =  {
        'com' : from_file(f'comms_{lbl}'),
        'opn' : [from_file(fn) for fn in data_opn_files(lbl)],
        'vfy' : [from_file(fn) for fn in data_vfy_files(lbl)]
    }

    # add ammortized times
    basic_record['amort'] = [extend_to_amm(basic_record, m) for m in N_AMORTS]
    #print(lbl)
    #print(basic_record['amort'])

    return basic_record


data = { lbl : mk_record(lbl) for lbl in LBLs }

plt_info = {}

# order in lst is the one in LBLs
def add_plot_info(info_lbl, lst):
    global plt_info
    plt_info[info_lbl] = {LBLs[i] : lst[i] for i in range(3) }

add_plot_info('color', ['red', 'orange', 'green'])
add_plot_info('marker', ['', '+', 'x'])
add_plot_info('amort_marker', ['.', '+', 'x'])
add_plot_info('lbl', ['This work\n(precomp.)', 'This work', 'BBF18'])

def get_data(c, s, opn_aux):
    if opn_aux is None:
        return data[s][c]
    else:
        return data[s][c][opn_aux]

def mk_plt(ax, plotName, cat, scmLbls, opn_aux = None):
    X = V_SZs


    
    ax.grid(True)
    ax.set(
        title = plotName,
        ylabel = "Running Time in Seconds",
        xlabel = 'Size of Committed Vector in Bits (log scale)',
        xscale = "log",
        xlim = (X[0]-3000, X[-1]+300000),
        yscale = "log")
    ax.set_xticks(X)
    ax.set_xticklabels(X)

    if cat == 'opn' and opn_aux == 2:
        X = X[2:]
        

    for scm in scmLbls:
        d = get_data(cat, scm, opn_aux)
        # cut openings that are too small:
        if cat == 'opn' and opn_aux == 2:
            d = d[2:]
            
        ax.plot(
            X,
            d, 
            marker = plt_info['marker'][scm],
            color = plt_info['color'][scm],
            label = plt_info['lbl'][scm])
        ax.legend()

def mk_plt_amort(ax, plotName, scmLbls, opn_aux = None):
    X = N_AMORTS
    
    ax.grid(True)
    ax.set(
        title = plotName,
        ylabel = "Running Time in Seconds",
        xlabel = '# of amortized openings',
        #xscale = "log",
        yscale = "log",
        #ylim = (2, 60),
        )
    #ax.set_xticks(X)
    #ax.set_xticklabels(X)

    #ax.set_yticks([10**i for i in range(1, 2)])
    ax.set_yticklabels([1, 5, 10, 25, 50, 100])



    for scm in scmLbls:
        d = get_data('amort', scm, opn_aux)
        ax.plot(
            X,
            d, 
            marker = plt_info['amort_marker'][scm],
            color = plt_info['color'][scm],
            label = plt_info['lbl'][scm])
        ax.legend()


if __name__ == '__main__':
    cmds = ['com', 'opn', 'amort']
    if len(argv) < 2 or not argv[1] in cmds:
        print("Give a command: com, opn, amort")
        exit(1)
    
    if argv[1] == 'com':
        fig, axs = plt.subplots(1, 1, figsize = (8,5.5))
        axcomm = axs

        # No preprocessing commitment plot
        mk_plt(axcomm, "Commitment (No Preprocessing)", 'com', ['yy', 'bbf'])
    elif argv[1] == 'opn':
        fig, axs = plt.subplots(3, 1, figsize = (5, 8))

        # Opening commitment
        for i in range(3):
            opn_aux = OPN_SZs[i]

            # Opening 
            mk_plt(axs[i], f"Opening (# of bits open = {opn_aux})",
                'opn', LBLs, opn_aux = i)

    elif argv[1] == 'amort':
        fig, axs = plt.subplots(1, 1, figsize = (7.5, 5))

        # Amortized times
        mk_plt_amort(axs, f"Amortized Opening (of {OPN_SZs[opn_idx]} bits)", LBLs)


    plt.tight_layout(pad=1, w_pad=1.5, h_pad=1.5)
    plt.show()