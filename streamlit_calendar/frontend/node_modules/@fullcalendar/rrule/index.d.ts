import { DateInput, PluginDef } from '@fullcalendar/core';
import { Options } from 'rrule';
import { Identity, createDuration } from '@fullcalendar/core/internal';

type RRuleInputObjectFull = Omit<Options, 'dtstart' | 'until' | 'freq' | 'wkst' | 'byweekday'> & {
    dtstart: Options['dtstart'] | DateInput;
    until: Options['until'] | DateInput;
    freq: Options['freq'] | string;
    wkst: Options['wkst'] | string;
    byweekday: Options['byweekday'] | string | string[];
};
type RRuleInputObject = Partial<RRuleInputObjectFull>;
type RRuleInput = RRuleInputObject | string;
declare const RRULE_EVENT_REFINERS: {
    rrule: Identity<RRuleInput>;
    exrule: Identity<Partial<RRuleInputObjectFull> | Partial<RRuleInputObjectFull>[]>;
    exdate: Identity<DateInput | DateInput[]>;
    duration: typeof createDuration;
};

type ExtraRefiners = typeof RRULE_EVENT_REFINERS;
declare module '@fullcalendar/core/internal' {
    interface EventRefiners extends ExtraRefiners {
    }
}
//# sourceMappingURL=ambient.d.ts.map

declare const _default: PluginDef;
//# sourceMappingURL=index.d.ts.map

export { _default as default };
